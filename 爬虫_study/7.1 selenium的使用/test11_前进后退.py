import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
browser.get('https://www.baidu.com/')
browser.back()
time.sleep(3)
browser.forward()
