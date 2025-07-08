import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://training.qaonlinetraining.com/testPage.php")

alert_button = driver.find_element(By.ID, "alert")
alert_button.click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert1 = driver.switch_to.alert
alert1.accept()

driver.find_element(By.ID, "confirm").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert2 =  driver.switch_to.alert
alert2.dismiss()

driver.find_element(By.ID, "prompt").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert3 = driver.switch_to.alert
print(f"The text from the alert box: {alert3.text}")
alert3.send_keys("John Doe")
alert3.accept()