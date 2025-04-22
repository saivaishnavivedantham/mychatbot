# main.py


from src.chatbot import answer_question

file_paths = [
    r"C:\Users\Sai Vaishnavi\Downloads\my_python_chatbot\data\Mark Lutz - Learning Python-O'Reilly Media (2007).pdf"
]

print("Welcome to the Python Assistant! Ask a question related to the textbook, or type 'exit' to quit.")

try:
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer = answer_question(file_paths, question)
        print("Assistant:", answer)
except Exception as e:
    print("An error occurred:", e)
