from langchain_ollama.chat_models import ChatOllama

model = ChatOllama(model = "llama3.2:1b")

messages = [
    {
        "role": "user",
        "content": "Why is the sky blue?"
    }
]

response = model.invoke(messages)

print(response.content)
