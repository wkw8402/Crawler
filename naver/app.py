import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

soup = BeautifulSoup(data.content, 'html.parser')
print( soup.find_all('strong', id="_nowVal")[0].text )
print( soup.find_all('span', class_="tah")[5].text )

# print out present price, trading volume of Samsung Electronics