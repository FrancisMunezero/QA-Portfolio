from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

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

driver.find_element(By.NAME, "bike").click()
driver.find_element(By.NAME, "boat").click()
driver.find_element(By.NAME, "horse").click()

country = driver.find_element(By.NAME, "country")
Select(country).select_by_visible_text("France")

skill = driver.find_element(By.NAME, "skill")
select_skill = Select(skill)
Select(skill).select_by_value("qa")
Select(skill).select_by_value("prg")

send = driver.find_element(By.CLASS_NAME, "special")
send.click()

