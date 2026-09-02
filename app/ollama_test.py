from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


response = llm.invoke(
    "What is diabetes? Explain it in simple words."
)


print(response.content)

