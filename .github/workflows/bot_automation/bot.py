import requests
import time

HEADERS = {
    'Authorization': 'Bearer YOUR_TOKEN_HERE',
    'Content-Type': 'application/json'
}

while True:
    response = requests.post('https://app.example.com/api/wallet/add', json={"amount": 1000}, headers=HEADERS)
    print(f"{time.ctime()}: {response.json()}")
    time.sleep(5)
