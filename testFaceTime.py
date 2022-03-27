from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from utils import get_facetime_url, get_steps
import time
from followSteps import perform_steps

# creating chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt)
# driver = webdriver.Firefox()

# Pynput configuration

def login():
    time.sleep(2)
    print('Starting')
    perform_steps(get_steps())


driver.get(get_facetime_url())

driver.implicitly_wait(20)

login()
