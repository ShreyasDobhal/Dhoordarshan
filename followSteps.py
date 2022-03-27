from pynput.mouse import Button as MouseButton, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyController
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Pynput configuration
mouse = MouseController()
keyboard = KeyController()


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

def open_page(url):
    global driver
    driver = webdriver.Chrome(options=opt)

    # config_camera_url = "chrome://settings/content/camera"
    # driver.get(config_camera_url)
    # sleep(3)  # Wait until selector appears
    # selector = driver.execute_script(
    #     "return document.querySelector('settings-ui')"
    #     ".shadowRoot.querySelector('settings-main')"
    #     ".shadowRoot.querySelector('settings-basic-page')"
    #     ".shadowRoot.querySelector('settings-section > settings-privacy-page')"
    #     ".shadowRoot.querySelector('settings-animated-pages > settings-subpage > media-picker')"
    #     ".shadowRoot.querySelector('#picker > #mediaPicker')"
    #     ".value = 'v4l2loopback'"  # Change for your default camera
    # )

    driver.get(url)
    driver.implicitly_wait(20)

def perform_steps(steps_map):
    for step in steps_map:
        action, param = step
        print(f"{action} {param}")
        if action == 'jump':
            mouse.position = param
        elif action == 'click':
            if param == 'left':
                mouse.click(MouseButton.left, 1)
            else:
                mouse.click(MouseButton.right, 1)
        elif action == 'double':
            if param == 'left':
                mouse.click(MouseButton.left, 2)
            else:
                mouse.click(MouseButton.right, 2)
        elif action == 'type':
            keyboard.type(param)
        elif action == 'delay':
            sleep(param)
        elif action == 'open':
            open_page(param)
        sleep(1)