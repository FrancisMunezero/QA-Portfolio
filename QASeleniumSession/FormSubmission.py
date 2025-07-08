from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)

driver.get("https://training.qaonlinetraining.com/testPage.php")
name = driver.find_element(By.NAME, "name")
name.send_keys("John Doe")

user_email = driver.find_element(By.ID, "eml")
user_email.send_keys("johndoe@gmail.com")

website = driver.find_element(By.NAME, "website")
website.send_keys("www.google.com")

comment = driver.find_element(By.NAME, "comment")
comment.send_keys("Thank you")

radio_button = driver.find_element(By.XPATH,'/html/body/form/input[4]')
radio_button.click()
if radio_button.is_selected():
    print("True")
else:
    print("False")

send = driver.find_element(By.CLASS_NAME, "special")
send.click()

