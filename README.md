# Personal AI Chatbot

## About

Personal AI Chatbot is an AI-powered application built using modern Generative AI technologies.  
It enables users to interact with multiple data sources such as the internet, personal databases, documents, and images using simple natural language queries.

The goal of this chatbot is to provide a single unified interface for querying structured and unstructured data efficiently.



## Key Features

- Web Intelligence  
  Ask questions and get answers from the internet using LLMs

- Database Interaction (MySQL)  
  Query relational databases using plain English instead of SQL  
  Automatic SQL generation using LangChain agents  
  Query result caching for improved performance

- Document Intelligence  
  Upload and query PDF, DOCX, XLSX, and PPTX files  
  Semantic search powered by vector embeddings

- Image Understanding  
  Upload single or multiple images  
  Ask questions about images using vision models

- Performance Optimizations  
  FAISS vector store for faster follow-up queries  
  Disk-based caching for database query results  
  Supports multiple documents and images in a single query


## Major Technologies Used

### Frontend / UI
- Streamlit  
  Rapid UI development framework for AI and ML applications

### LLM & Orchestration
- LangChain  
  Orchestrates LLM workflows, SQL agents, and retrieval-based question answering

### Large Language Models
- OpenAI  
  Used for text reasoning and SQL agents  
- Google Gemini  
  Used for web queries and image understanding

### Vector Database
- FAISS  
  Stores embeddings for semantic document search

### Document Parsing
- PyPDF2 – PDF text extraction  
- python-docx – Word document parsing  
- openpyxl – Excel file processing  
- python-pptx – PowerPoint slide text extraction  

### Database
- MySQL  
  Relational database queried using natural language


## How to Run (Step-by-Step)

### Step 1: Install Python
Ensure Python 3.10 is installed.

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone <your-repo-url>
cd personal-ai-chatbot
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### Step 5: Setup MySQL Database

Run `schema.sql` to create the database, tables, and sample records.

Ensure database credentials match:

```text
mysql://root:mysql123@localhost/personaldb
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

### Step 7: Open in Browser

```text
http://localhost:8501
```

## Application Snapshots

```md
![Home](screenshots/1.png)
![Web Query](screenshots/2.png)
![Database](screenshots/3.png)
![Database Query](screenshots/4.png)
![Document Query](screenshots/5.png)
![Image Query](screenshots/6.png)
```

## Future Enhancements

This application can be enhanced further with:

- Voice-based querying
- Authentication and user profiles
- Chat history persistence
- Cloud deployment (AWS, GCP, Azure)
- Memory-based conversations
- Much more as per business/project needs

Architecture Note:
At present, the application is built using Streamlit for the user interface. Going forward, the architecture can be enhanced by introducing a FastAPI-based backend for scalable RESTful services and a separate frontend using Angular or React to achieve better modularity and maintainability.


## License

Free Software, by [Siraj Chaudhary](https://www.linkedin.com/in/sirajchaudhary/)
