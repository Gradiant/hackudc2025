# CompetenciApp
## Potenciando tu aplicación con datos e IA

Este repositorio se corresponde con los ejercicios vistos en el Workshop impartido por [Gradiant](https://www.gradiant.org) en la [HackUDC 2025](https://hackudc.gpul.org).


## Ollama

Tras instalar [Ollama](https://github.com/ollama/ollama) podemos lanzar el servidor.

```bash
ollama serve
```

### Ollama Run

La forma más básica de interactuar con los modelos es lanzar uno desde la consola.

```bash
ollama run llama3.2:1b
```

### Ollama REST API

El servidor expone una API REST con la que también podremos interactuar. La API ya nos empieza a ofrecer más flexibilidad para realizar tareas de forma programática.

#### CURL

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2:1b",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false
}'
```


#### Python

```bash
pip install requests
```

```python
import requests

url = 'http://localhost:11434/api/chat'

data = {
  "model": "llama3.2:1b",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": False
}

response = requests.post(url, json=data)
print(response.text)
```

### Ollama SDK

Utilizaremos el SDK de Python: [ollama-python](https://github.com/ollama/ollama-python)

```bash
pip install ollama
```

```python
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2:1b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

print(response.message.content)
```

### LangChain

[LangChain repository](https://github.com/langchain-ai/langchain)

LangChain nos ofrece la posibilidad de hacer pipelines de manera sencilla y tiene integración con Ollama.

```bash
pip install langchain
pip install langchain-ollama
```

```python
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
```

### LangChain: Plantillas

```python
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
```


### LangChain: Datos estructurados

```python
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
```

### Tip para el reto

```python
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
```


## Otras fuentes de datos

### CLOC

[CLOC](https://github.com/AlDanial/cloc) es una herramienta para contar líneas de código pero nos ofrece la posibilidad de detectar el lenguaje.

```bash
cloc README.md
```

```bash
cloc ./ --by-file --csv --quiet --report-file=cloc_report.csv
```

### Git Log

Git log nos muestra el historial de cambios del repo.

```bash
git log
```

Podemos hacer un listado de personas que han modificado un fichero ...

```bash
git log --pretty=format:'%an' -- README.md | sort -u
```

### Git Blame

Git blame nos dice quién ha modificado cada línea de código de un fichero

```bash
git blame README.md
```

Jugando con los parámetros podemos aislar el nombre de quien ha modificado una línea concreta ...

```bash
git blame --porcelain -L 5,5 README.md | sed -n 's/^author //p'
```
