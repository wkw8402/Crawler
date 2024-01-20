from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome('/Users/kyungwanwoo/Desktop/Crawler/instagram/chromedriver')
driver.get('https://instagram.com')

# Log in
time.sleep(3)
e = driver.find_element_by_css_selector('input[name="username"]')
e.send_keys('crack_19162423')
e = driver.find_element_by_css_selector('input[name="password"]')
e.send_keys('crackmalkin1223')
e.send_keys(Keys.ENTER)

time.sleep(3)
# Move to #apple page
driver.get('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/')
# Click on first image
driver.implicitly_wait(10) 
e = driver.find_element_by_css_selector('._aagw').click()

for i in range(10):
    # Save image
    image = driver.find_element_by_css_selector('._aagw').get_attribute('src')
    urllib.request.urlretrieve(image, f'{i}.jpg')

    # Next
    e = driver.find_element_by_css_selector('._aagw')
    driver.execute_script('arguments[0].click();', e)


# time.sleep(2)
# e = driver.find_element_by_css_selector('._ab37').text
# n = driver.find_element_by_css_selector('input[name="username"]').text
# print(e)
