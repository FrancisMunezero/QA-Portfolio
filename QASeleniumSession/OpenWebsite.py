from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option( "detach", True )
driver = webdriver.Chrome(options=options)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")