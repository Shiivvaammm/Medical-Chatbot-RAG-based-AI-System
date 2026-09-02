from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


# Load PDF
pdf_path = "data/Diabetes WHO.pdf"

loader = PyPDFLoader(pdf_path)

documents = loader.load()


# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


# Split documents into chunks
chunks = text_splitter.split_documents(documents)


print("Number of pages:", len(documents))
print("Number of chunks:", len(chunks))


# Display first chunk
print("\nFirst chunk:\n")
print(chunks[0].page_content)


# Display metadata
print("\nFirst chunk metadata:\n")
print(chunks[0].metadata)