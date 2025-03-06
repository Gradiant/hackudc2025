from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model = "llama3.2:1b", temperature = 0)

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

message = {"language": "Spanish", "text": "Car is blue"}

prompt = prompt_template.invoke(message)

response = model.invoke(prompt)

print(response.content)


