from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Load environment variables from .env
load_dotenv()

# Retrieve API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI chat model
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.2,  # Low randomness for consistent answers
)

# Initialize OpenAI embeddings model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
