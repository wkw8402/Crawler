import requests
import json
import time

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1701964800000&interval=1H&1705563554385')
# print(data.content)

dictionary = json.loads(data.content)
for i in range(200):
    dt = dictionary['body']['candles'][i]['dt']
    textTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dt/1000))
    # remove last 3 digits = miliseconds

    print(textTime)
    print(dictionary['body']['candles'][i]['close'])
