from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from utils import get_meeting_id
import time


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

# opt.add_argument("--disable-infobars")
# opt.add_argument("start-maximized")
# opt.add_argument("--disable-extensions")
# # Pass the argument 1 to allow and 2 to block
# opt.add_experimental_option("prefs", { \
# "profile.default_content_setting_values.media_stream_mic": 1, 
# "profile.default_content_setting_values.media_stream_camera": 1,
# "profile.default_content_setting_values.geolocation": 1, 
# "profile.default_content_setting_values.notifications": 1 
# })


driver = webdriver.Chrome(options=opt)
# driver = webdriver.Firefox()

def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    driver.find_element(
        By.XPATH,
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
        # '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(3000)
 
    # turn off camera
    time.sleep(1)
    driver.find_element(
        By.XPATH,
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
        # '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(3000)

def AskToJoin():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element(
        By.XPATH,
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[1]/div[3]/div[1]/div/div[1]/input').send_keys('Guest')
    # Ask to join and join now buttons have same xpaths
    driver.implicitly_wait(2000)
    driver.find_element(
        By.XPATH,
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span').click()
    


# driver = webdriver.Chrome()

# driver.maximize_window()
# driver.get("https://google.com")

driver.get(f"https://meet.google.com/{get_meeting_id()}")
turnOffMicCam()
AskToJoin()