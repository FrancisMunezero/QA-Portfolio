import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
time.sleep(2)
mySearch = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
mySearch.send_keys("Francis Munezero")
time.sleep(2)
mySearch.submit()