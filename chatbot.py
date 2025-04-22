# src/chatbot.py
from src.data_loader import load_and_split_textbooks
from src.embed_and_index import create_index
from src.retriever import retrieve
from src.generator import generate_answer

def answer_question(file_paths, question):
    # Step 1: Load and split the textbooks
    texts = load_and_split_textbooks(file_paths)
    print(f"Loaded {len(texts)} text chunks")  # Debug

    # Step 2: Create the index (reuse if already created)
    model, index = create_index(texts)
    print("Index created successfully.")  # Debug

    # Step 3: Retrieve relevant texts
    retrieved_texts = retrieve(question, model, index, texts, k=3)  # Retrieve top 3 chunks
    if retrieved_texts:
        print("Retrieved Context:", " ".join(retrieved_texts))  # Debug
    else:
        print("No relevant context retrieved.")  # Debug

    # Step 4: Generate the answer

    context = " ".join(set(retrieved_texts[:3]))[:1000]  # Limit context to 1000 characters


    answer = generate_answer(context, question)
    print("Generated Answer:", answer)  # Debug
    return answer
