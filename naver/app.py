import requests
from bs4 import BeautifulSoup
import urllib.request

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

soup = BeautifulSoup(data.content, 'html.parser')
print( soup.find_all('strong', id="_nowVal")[0].text )
print( soup.find_all('span', class_="tah")[5].text )

# print out present price, trading volume of Samsung Electronics

# css selector => class = .   id = #

# find em tag inside f_down class
print( soup.select('.f_down em')[0].text )

# download image
image = soup.select('#img_chart_area')[0]
print( image['src'] )
urllib.request.urlretrieve(image['src'], 'image')

