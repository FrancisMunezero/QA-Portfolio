from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get("https://www.google.com")
url = driver.find_element(By.LINK_TEXT, "Grafika")
url.click()

