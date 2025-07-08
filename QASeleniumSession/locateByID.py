from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option( "detach", True )
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
search_box = driver.find_element(By.ID, "APjFqb")
search_box.send_keys("Oliwia Bielawska")
search_box.submit()

