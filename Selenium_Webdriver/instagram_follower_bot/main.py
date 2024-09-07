from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

USER_NAME = 'send.test02'
PASSWORD = '1234@asdf'
TARGET_ACCOUNT = 'cbum'

chrome_options = webdriver.ChromeOptions()

class InstaFollower:
    def __init__(self, chrome):
        self.chrome_path = chrome
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= self.chrome_path)
    
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        self.user_name = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.user_name.send_keys(USER_NAME)
        sleep(1)
        self.password = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password.send_keys(PASSWORD)
        sleep(1)
        self.password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(3)
        self.driver.get(f'https://www.instagram.com/{TARGET_ACCOUNT}/followers')
        sleep(3)
        self.followers_list = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,'_aano')))

        for _ in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight',self.followers_list)
            sleep(2)

    def follow(self):
        self.follow_buttons = self.driver.find_elements(by=By.CLASS_NAME, value='_aaes')
        #When clicking a button, choose a div that surrounds it, not the button!! always remember its a section above the thing
        sleep(2)
        for button in self.follow_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                sleep(1)
                cancel_button = self.driver.find_element(by=By.XPATH, value='//*[@id="mount_0_0_jJ"]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
                cancel_button.click()

instagram_bot = InstaFollower(chrome_options)
instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()