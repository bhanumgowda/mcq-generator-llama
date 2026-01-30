from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

response = llm.invoke("Explain cloud computing in one line")

print(response)
