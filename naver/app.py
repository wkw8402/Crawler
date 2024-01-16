import requests
from bs4 import BeautifulSoup
import urllib.request

def presentPrice(code):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={code}')
    soup = BeautifulSoup(data.content, 'html.parser')
    return soup.find_all('strong', id="_nowVal")[0].text, soup.find_all('span', class_="tah")[5].text

# prints out present price, trading volume of Samsung Electronics and LG Electronics
Snow, Svol = presentPrice('005930')
Lnow, Lvol = presentPrice('066575')

f = open('a.txt', 'w')
f.write

# css selector => class = .   id = #

# # find em tag inside f_down class
# print( soup.select('.f_down em')[0].text )

# # download image
# image = soup.select('#img_chart_area')[0]
# print( image['src'] )
# urllib.request.urlretrieve(image['src'], 'image')

