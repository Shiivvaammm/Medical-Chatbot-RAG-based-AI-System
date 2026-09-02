from langchain_community.document_loaders import PyPDFLoader

pdf_path = "data/Diabetes WHO.pdf"

loader = PyPDFLoader(pdf_path)

documents = loader.load()

print("Number of pages:", len(documents))

print("\nFirst page content:\n")
print(documents[0].page_content[:1000])

print("\nFirst page metadata:\n")
print(documents[0].metadata)