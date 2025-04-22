# src/data_loader.py
import fitz  # PyMuPDF for PDF processing
from langchain.text_splitter import CharacterTextSplitter

# Define a simple Document class for storing page content
class Document:
    def __init__(self, page_content):
        self.page_content = page_content

def load_and_split_textbooks(file_paths):
    documents = []
    for file_path in file_paths:
        pdf_document = fitz.open(file_path)
        for page in pdf_document:
            text = page.get_text("text")
            if text.strip():  # Only include non-empty text
                documents.append(text)
        pdf_document.close()

    # Concatenate all pages into a single string for splitting
    combined_text = "\n".join(documents)

    # Split the combined text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=100
    )
    texts = text_splitter.split_text(combined_text)  # Corrected to pass a single string

    return [Document(page_content=text) for text in texts]
