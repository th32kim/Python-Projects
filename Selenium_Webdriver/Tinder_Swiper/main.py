from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

EMAIL = 'richard.kim0321@gmail.com'
PASSWORD = '1126679@asdf'

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://tinder.com/')
sleep(1)
login = driver.find_element(by=By.XPATH, value='//*[@id="o-654199900"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
sleep(2)
fb_login = driver.find_element(by=By.XPATH, value='//*[@id="o1912386320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login.click()
sleep(1)

#FB Login -- New window - have to change it
base_window = driver.window_handles[0]
fb_login_page = driver.window_handles[1]
driver.switch_to.window(fb_login_page)

email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
password = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
login_button = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[2]/a')
login_button.click()



sleep(10000)