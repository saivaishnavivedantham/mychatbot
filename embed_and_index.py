# src/embed_and_index.py
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import torch

def create_index(texts, batch_size=100):
    print("Starting to generate embeddings...")  # Debug
    # Ensure the model uses GPU if available
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = SentenceTransformer('paraphrase-MiniLM-L3-v2', device=device)

    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch_texts = [text.page_content for text in texts[i:i + batch_size]]
        batch_embeddings = model.encode(batch_texts)
        all_embeddings.extend(batch_embeddings)

    embeddings = np.array(all_embeddings)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print("Index created with FAISS.")  # Debug
    return model, index
