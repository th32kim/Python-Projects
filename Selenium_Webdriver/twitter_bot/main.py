from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'richard.kim0321@gmail.com'
TWITTER_USER = '@Kim0321Richard'
TWITTER_PASSWORD = '1126679@asdf'
chrome_options = webdriver.ChromeOptions()


class InternetSpeedTwitterBot:
    def __init__(self, chrome):
        self.chrome_path = chrome
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= self.chrome_path)
        self.up = 0
        self.down=0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(3)
        self.go_button = self.driver.find_element(by=By.CLASS_NAME, value='start-text')
        self.go_button.click()
        sleep(45)
        self.down_value= self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = self.down_value.text
        self.upl_value = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = self.upl_value.text
        self.driver.close()

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')

        #Twitter_login
        sleep(2)
        self.signin = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        self.signin.click()
        sleep(2)
        self.email = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.email.send_keys(TWITTER_EMAIL)
        sleep(2)
        self.next_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        self.next_button.click()
        sleep(30)
        #_________________Manual Input__________________
        # self.user_name = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input')
        # self.user_name.send_keys(TWITTER_USER)
        # sleep(2)
        # self.next = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        # self.next.click()
        self.password = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        self.login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        self.login_button.click()
        sleep(2)
        #Sending Twitt
        draft = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        draft.send_keys('Hello World')

bot = InternetSpeedTwitterBot(chrome_options)
# bot.get_internet_speed()
bot.tweet_at_provider()



