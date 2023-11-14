from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

browser =webdriver.Chrome()
try:
    browser.get('https://www.baidu.com/')
except TimeoutException:
    print('TIME Out!')
try:
    browser.find_element(By.ID,'hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.quit()