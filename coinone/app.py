import requests
import json
import time

def close():
    data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1701964800000&interval=1H&1705563554385')
    # print(data.content)

    dictionary = json.loads(data.content)
    for i in range(200):
        dt = dictionary['body']['candles'][i]['dt']
        textTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dt/1000))
        # remove last 3 digits = miliseconds

        print(textTime)
        print(dictionary['body']['candles'][i]['close'])

from multiprocessing.dummy import Pool as ThreadPool

def multithreading():
    url = [
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
    ]

    pool = ThreadPool(4)
    result = pool.map(function1, url)
    pool.close()
    pool.join()
    
    print(result)

def function1(url):
    data = requests.get(url)
    dictionary = json.loads(data.content)
    return dictionary['data'][0]['Close']

multithreading()

