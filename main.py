from langchain_ollama import OllamaLLM
from prompt import build_prompt

print("===== MCQ Generator using LLaMA =====")

# User inputs
topic = input("Enter Topic: ")
num_questions = int(input("Enter Number of Questions: "))
level = input("Enter Difficulty (Easy / Medium / Hard): ")

# Load LLaMA model
llm = OllamaLLM(model="llama3")

# Build the prompt
prompt = build_prompt(topic, num_questions, level)

print("\nGenerating MCQs...\n")

# Call LLaMA
response = llm.invoke(prompt)

# Output
print(response)
