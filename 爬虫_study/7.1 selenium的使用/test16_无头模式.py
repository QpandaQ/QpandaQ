import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.set_window_size(1366,768)
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('preview.png')
time.sleep(5)
