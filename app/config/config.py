import os

# 🔑 OpenAI (LLM)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# 📦 Vector store
DB_FAISS_PATH = "vectorstore/db_faiss"

# 📄 Data
DATA_PATH = "data/"

# ✂️ Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

