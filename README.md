## 🤖 Chatbot with Retrieval-Augmented Generation (RAG)
**📅 Duration:** Oct 2024 – Jan 2025  
**📍 Institution:** UTA  

A Python chatbot capable of answering programming questions using semantic search and generative models.

### ✨ Highlights
- Parsed textbook PDFs using **PyMuPDF** and chunked content via **LangChain**.
- Generated dense embeddings using **SentenceTransformers** and indexed with **FAISS**.
- Applied **TF-IDF filtering** for refined retrieval results.
- Deployed a **DistilGPT-2** language model for response generation.
- Served through **FastAPI**; achieved a 35% faster response time via optimized embeddings.

### 🧠 Architecture
1. **Document Parsing** → PDF to text (PyMuPDF)
2. **Chunking & Embedding** → LangChain + SentenceTransformers
3. **Retrieval** → FAISS + TF-IDF Filtering
4. **Generation** → DistilGPT-2 (HuggingFace)
5. **Serving** → FastAPI API Endpoint

### 🛠️ Tech Stack
`Python`, `FAISS`, `LangChain`, `HuggingFace Transformers`, `FastAPI`, `PyMuPDF`, `SentenceTransformers`

### 📊 Results
- ✅ Reduced latency by 35%
- 📚 Accurately answered textbook-level Python questions
