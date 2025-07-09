from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get('https://the-internet.herokuapp.com/drag_and_drop')

source = driver.find_element(By.ID, 'column-a')
target = driver.find_element(By.ID, 'column-b')

action = ActionChains(driver)
action.drag_and_drop(source,target).perform()

