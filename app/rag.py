import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama


# --------------------------------------------------
# 1. Sources
# --------------------------------------------------

SOURCE_NAMES = {
    "Diabetes WHO.pdf": {
        "title": "Guidance on global monitoring for diabetes prevention and control-2024",
        "publisher": "World Health Organization",
        "isbn": "9240102248"
    },

    "Hypertension WHO.pdf": {
        "title": "Guideline for the pharmacological treatment of hypertension in adults",
        "publisher": "World Health Organization",
        "year": "2021",
        "isbn": "978-92-4-003398-6"
    },

    "Asthma WHO.pdf": {
        "title": "Tobacco and asthma: WHO tobacco knowledge summaries",
        "publisher": "World Health Organization",
        "year": "2024",
        "isbn": "978-92-4-009753-7"
    }
}


# --------------------------------------------------
# 2. Embedding model
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 3. Connect to ChromaDB
# --------------------------------------------------

vectorstore = Chroma(
    collection_name="medical_documents",
    persist_directory="chroma_db",
    embedding_function=embeddings
)


# --------------------------------------------------
# 4. Ollama
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 5. RAG function
# --------------------------------------------------

def ask_medical_question(query: str):

    results = vectorstore.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        document.page_content
        for document in results
    )

    prompt = f"""
You are a medical information assistant.

Answer the user's question using ONLY the
information provided in the context.

If the answer cannot be found in the context,
say that the information is not available
in the provided medical documents.

Do not diagnose the user.

Do not prescribe medicines or dosages.

For emergencies, advise the user to seek
immediate professional medical help.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    # --------------------------------------------------
    # 6. Collect sources
    # --------------------------------------------------

    sources = []

    for document in results:

        source_path = document.metadata.get("source")

        if not source_path:
            continue

        document_name = os.path.basename(source_path)

        source_info = SOURCE_NAMES.get(document_name)

        if source_info:

            source = {
                "document": source_info["title"],
                "publisher": source_info["publisher"],
                "page": document.metadata.get("page")
            }

            if "year" in source_info:
                source["year"] = source_info["year"]

            if "isbn" in source_info:
                source["isbn"] = source_info["isbn"]

            sources.append(source)

    return {
        "answer": response.content,
        "sources": sources
    }