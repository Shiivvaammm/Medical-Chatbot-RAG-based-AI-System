import glob

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# 1. Find all PDF files

pdf_files = glob.glob("data/*.pdf")

print("PDF files found:")

for pdf in pdf_files:
    print("-", pdf)


# 2. Load all PDFs

documents = []

for pdf_path in pdf_files:

    print(f"\nLoading: {pdf_path}")

    loader = PyPDFLoader(pdf_path)

    pdf_documents = loader.load()

    documents.extend(pdf_documents)


print("\nTotal pages loaded:", len(documents))


# 3. Split documents into chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)


print("Total chunks created:", len(chunks))


# 4. Create embedding model

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 5. Store chunks in ChromaDB

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db",
    collection_name="medical_documents"
)


print("\nSuccessfully stored documents in ChromaDB!")