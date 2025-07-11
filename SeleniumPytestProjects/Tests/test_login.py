import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SeleniumPytestProjects.Pages.login import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    yield driver
    time.sleep(4)
    driver.quit()

def test_login_valid(driver):
    page = LoginPage(driver)
    page.load()
    page.login('tomsmith','SuperSecretPassword!')
    assert "Secure Area" in driver.page_source
