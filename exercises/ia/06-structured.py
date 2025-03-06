from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model = "llama3.2:1b", temperature = 0)

from pydantic import BaseModel, Field
class ResponseFormatter(BaseModel):
    item: str = Field(description="The object refered in the sentence")
    color: str = Field(description="The color of the object")

model_with_structure = model.with_structured_output(ResponseFormatter)

message = "The car is blue."

structured_output = model_with_structure.invoke(message)

print(structured_output.model_dump_json())



