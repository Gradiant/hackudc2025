from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model = "llama3.2:1b", temperature = 0)

from pydantic import BaseModel, Field
class ResponseFormatter(BaseModel):
    action: str = Field(description="The action that took place")
    item: str = Field(description="The element that the action refers to")
    date: str = Field(description="Relative days ago when the action took place")

model_with_structure = model.with_structured_output(ResponseFormatter)

message = "I've watched a microservices tutorial two days ago."

structured_output = model_with_structure.invoke(message)

print(structured_output.model_dump_json())



