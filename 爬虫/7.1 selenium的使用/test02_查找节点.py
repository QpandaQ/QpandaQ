from selenium import webdriver
from selenium.webdriver.common.by import By

brower = webdriver.Chrome()
brower.get('https://www.taobao.com')
input_first = brower.find_element(By.ID, 'q')
input_second = brower.find_element(By.CSS_SELECTOR, '#q')
input_third = brower.find_element(By.XPATH, '//*[@id="q"]')
print(input_third,input_first,input_second)
brower.close()