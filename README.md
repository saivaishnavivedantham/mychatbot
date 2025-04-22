🤖 Chatbot with Retrieval-Augmented Generation (RAG)
📅 Oct 2024 – Jan 2025
Built a semantic chatbot that answers Python programming questions using vector search and generative models.

🚀 Features
Used PyMuPDF to parse Python textbooks and LangChain for smart document chunking.

Generated dense embeddings using SentenceTransformers; indexed with FAISS for similarity search.

Applied TF-IDF filtering to enhance query-context relevance.

Used DistilGPT-2 via HuggingFace for generative responses.

Deployed with FastAPI, reduced latency by 35% through query and embedding tuning.

🧠 Architecture
Data Preprocessing → PDF parsing → Text chunking

Embedding Generation → SentenceTransformers

Indexing & Retrieval → FAISS + TF-IDF

Response Generation → DistilGPT-2

API Serving → FastAPI

📦 Tech Stack
Python, FAISS, LangChain, SentenceTransformers, FastAPI, HuggingFace, PyMuPDF

📈 Results
35% faster response time

Highly contextual answers based on textbook understanding

