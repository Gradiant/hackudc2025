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
