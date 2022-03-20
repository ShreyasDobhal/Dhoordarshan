from selenium import webdriver
from utils import get_meeting_id

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://google.com")
