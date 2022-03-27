from selenium import webdriver
from utils import get_googlemeet_url

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://google.com")

# http://archive.raspberrypi.org/debian/pool/main/c/chromium-browser/chromium-browser-dbgsym_92.0.4515.98-rpt1_arm64.deb