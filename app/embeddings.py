from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


text = "What are the symptoms of diabetes?"

vector = embeddings.embed_query(text)

print("Vector length:", len(vector))

print("\nFirst 10 values:")
print(vector[:10])