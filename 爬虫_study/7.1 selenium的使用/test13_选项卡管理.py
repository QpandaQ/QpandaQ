import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
browser.execute_script('window.open()')
# 选项卡
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.baidu.com/')
time.sleep(3)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')