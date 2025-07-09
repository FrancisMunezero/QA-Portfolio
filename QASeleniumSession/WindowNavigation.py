import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
time.sleep(2)

driver.switch_to.new_window()
driver.get("https://demo.itlearn360.com")
time.sleep(2)

number_tabs = len(driver.window_handles)
print(number_tabs)

tab_values = driver.window_handles
print(tab_values)

currentTab_value = driver.current_window_handle
print(currentTab_value)

driver.find_element(By.XPATH, '//*[@id="loginlabel"]').click()
time.sleep(2)

first_tab = tab_values[0]
driver.switch_to.window(first_tab)

driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
driver.find_element(By.LINK_TEXT, 'Gmail').click()

driver.quit()

