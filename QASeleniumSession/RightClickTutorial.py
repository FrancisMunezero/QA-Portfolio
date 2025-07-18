from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')

right_click = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span')
action = ActionChains(driver)
action.context_click(right_click).perform()


