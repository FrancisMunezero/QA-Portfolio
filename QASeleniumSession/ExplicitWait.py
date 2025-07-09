from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

gmail = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Gmail'))
    )
driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
gmail.click()

