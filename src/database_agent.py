import os
import json
import hashlib

from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from utils.config import llm


# Directory to store cached SQL results
SQL_CACHE_DIR = "sql_cache"
os.makedirs(SQL_CACHE_DIR, exist_ok=True)


# Initialize DB connection
db = SQLDatabase.from_uri(
    "mysql://root:mysql123@localhost/personaldb",
    sample_rows_in_table_info=6,
)


# Create toolkit with DB + LLM
toolkit = SQLDatabaseToolkit(db=db, llm=llm)


# Create SQL agent to convert natural language to SQL and run queries
sql_agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    top_k=50,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)


# Generate stable hash for query caching
def _query_hash(query: str) -> str:
    return hashlib.sha256(query.encode("utf-8")).hexdigest()


# Load cached SQL result if available
def _load_cached_result(query: str):
    cache_file = os.path.join(SQL_CACHE_DIR, f"{_query_hash(query)}.json")
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


# Persist SQL result to disk
def _save_cached_result(query: str, result):
    cache_file = os.path.join(SQL_CACHE_DIR, f"{_query_hash(query)}.json")
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(result, f, default=str)


# Execute query with caching
def query_sql(query: str):

    # Return cached result if present
    cached = _load_cached_result(query)
    if cached is not None:
        return cached

    # Execute query via SQL agent
    result = sql_agent.run(query)

    # Persist result for future use
    _save_cached_result(query, result)

    return result
