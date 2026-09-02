from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# 1. Embedding model

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 2. Connecting to ChromaDB

vectorstore = Chroma(
    collection_name="medical_documents",
    persist_directory="chroma_db",
    embedding_function=embeddings
)


# 3. Ask question

query = input("\nAsk a medical question: ")


# 4. Search

results = vectorstore.similarity_search(
    query,
    k=3
)


# 5. Display results

for i, result in enumerate(results):

    print(f"\n========== RESULT {i + 1} ==========")

    print("\nContent:")
    print(result.page_content)

    print("\nSource:")
    print(result.metadata.get("source"))

    print("Page:")
    print(result.metadata.get("page"))