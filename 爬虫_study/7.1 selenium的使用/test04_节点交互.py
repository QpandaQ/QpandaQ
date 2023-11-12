import time

from selenium import webdriver
from selenium.webdriver.common.by import By

brower = webdriver.Chrome()
brower.get('https://www.taobao.com')
input_first = brower.find_element(By.ID, 'q')
input_first.send_keys('书')
time.sleep(2)
input_first.clear()
input_first.send_keys('iPad')
button = brower.find_element(By.CLASS_NAME, 'btn-search')
button.click()
time.sleep(2)
brower.close()