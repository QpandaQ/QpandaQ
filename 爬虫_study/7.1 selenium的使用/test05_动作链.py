import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

brower = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
brower.get(url)
brower.switch_to.frame('iFrameResult')
time.sleep(5)
source = brower.find_element(By.CSS_SELECTOR, '#draggable')
target = brower.find_element(by=By.CSS_SELECTOR, value='#droggable')
actions = ActionChains(brower)
actions.drag_and_drop(source, target)
time.sleep(5)
brower.close()