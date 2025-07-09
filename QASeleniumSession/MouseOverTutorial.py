import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.ebay.com")

mouse_over = driver.find_element(By.XPATH, '//*[@id="vl-flyout-nav"]/ul/li[7]/a')
action = ActionChains(driver)
action.move_to_element(mouse_over).perform()

driver.find_element(By.LINK_TEXT, "Streetwear").click()
time.sleep(2)

driver.quit()