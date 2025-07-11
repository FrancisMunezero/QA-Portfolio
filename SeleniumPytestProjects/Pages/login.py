from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.driver.find_element(By.ID  , "username").send_keys("tomsmith")
        self.driver.find_element(By.ID  , "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.XPATH , "//*[@id='login']/button/i").click()
