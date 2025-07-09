import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.itlearn360.com")
driver.implicitly_wait(10)

driver.find_element(By.ID, 'loginlabel').click()
driver.find_element(By.ID, 'user_login').send_keys('Demo12')
driver.find_element(By.ID, 'user_pass').send_keys('Test123456$')
driver.find_element(By.ID, 'wp-submit').click()
time.sleep(2)

driver.quit()
