import requests 
from bs4 import BeautifulSoup

def presentPrice(code):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={code}')
    soup = BeautifulSoup(data.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    print(soup.find_all('span', class_="tah")[5].text)
    return soup.find_all('strong', id="_nowVal")[0].text
    # prints out present price, trading volume of Compnay

companyCodes = ['005930', '066575', '005380', '035720', '034220', '003490']
# Samsung, LG, Hyundai, Kakao, LG Display, Korean Air

f = open('a.txt', 'w')

for i in range(6):
    f.write( '\n' + presentPrice( companyCodes[i] ) )

# css selector => class = .   id = #

# # find esudo pip3 install requests
#  tag inside f_down class
# print( soup.select('.f_down em')[0].text )

# # download image
# image = soup.select('#img_chart_area')[0]
# print( image['src'] )
# urllib.request.urlretrieve(image['src'], 'image')

