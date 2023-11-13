from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://spa2.scrape.center/'
browser.get(url)

logo = browser.find_element(by=By.CLASS_NAME, value='logo-image')
input = browser.find_element(By.CLASS_NAME, 'logo-title')
print(logo)
# 获取图片的src属性
print(logo.get_attribute('src'))
# 获取文本text
print(input.text)
print(input.id)
print(input.tag_name)
print(input.size)