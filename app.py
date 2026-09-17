import requests

url = "http://127.0.0.1:8081/message/sendText/fake-analyser"

payload = {
    "number": "5519982503536",
    "text": "Hello World!"  
}

headers = {
    "apikey": "1234",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)