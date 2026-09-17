import requests

url = "http://127.0.0.1:8081/message/sendText/fake-analyser"


payload = {
    "where": {
        "key": {
            # Digite o número do cliente com o formato do WhatsApp (@s.whatsapp.net)
            "remoteJid": "5519982503536@s.whatsapp.net"
        }
    },
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