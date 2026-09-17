import requests

url = "http://127.0.0.1:8081/message/sendText/fake-analyser"


payload = {
    "limit": 50,      # Quantidade de chats que você quer listar (ex: os últimos 50)
    "page": 1,
    
    "where": {},
    "take": 123,
    "skip": 123,
    "orderBy": {}
}

headers = {
    "apikey": "1234",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)