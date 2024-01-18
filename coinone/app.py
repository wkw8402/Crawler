import requests
import json

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1701964800000&interval=1H&1705563554385')
# print(data.content)

dictionary = json.loads(data.content)
print(dictionary['body']['candles'][0]['close'])
