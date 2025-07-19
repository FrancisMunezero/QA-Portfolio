import pytest
from selenium.webdriver.common.by import By


search_keywords = [
    "Selenium Pytest Framework",
    "Automation Testing pdf",
    "Playwright Tutorial"
]

@pytest.mark.parametrize("search_keyword", search_keywords)
class TestGoogleSearch:
    def test_google(self, browser, search_keyword):
        driver = browser
        driver.get("https://duckduckgo.com/")
        try:
            driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()
        except Exception:
            pass
        search_box = driver.find_element(By.ID, 'searchbox_input')
        search_box.send_keys(search_keyword)
        search_box.submit()
        assert search_keyword in driver.title