# src/retriever.py
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

def retrieve(query, model, index, texts, k=5):
    # Embed query
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    # Filter retrieved texts based on relevance to query keywords
    vectorizer = TfidfVectorizer()
    query_terms = vectorizer.fit([query]).get_feature_names_out()
    unique_indices = []
    for idx in indices[0]:
        chunk = texts[idx].page_content
        # Only include if it contains query terms
        if any(term in chunk for term in query_terms):
            unique_indices.append(idx)

    # Return filtered chunks of text
    return [texts[i].page_content for i in unique_indices[:k]]
