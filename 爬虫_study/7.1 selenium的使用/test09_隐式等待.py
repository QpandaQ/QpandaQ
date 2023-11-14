from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# implicitly_wait()实现隐式等待
browser.implicitly_wait(10)
browser.get('https://spa2.scrape.center/')
input = browser.find_element(By.CLASS_NAME, 'logo-image')
print(input)