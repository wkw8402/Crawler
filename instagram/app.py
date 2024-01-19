from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/kyungwanwoo/Desktop/Crawler/instagram/chromedriver')

driver.get('https://instagram.com')

time.sleep(2)
e = driver.find_element_by_css_selector('._ab37').text
print(e)
