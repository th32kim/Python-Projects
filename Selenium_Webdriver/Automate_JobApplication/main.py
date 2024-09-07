from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


EMAIL = 'richard8851@gmail.com'
PASSWORD='1234'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')
sign_in = driver.find_element(by=By.LINK_TEXT, value='Sign in')
sign_in.click()
time.sleep(3)
email=driver.find_element(by=By.ID, value='username')
email.send_keys(EMAIL)
password = driver.find_element(by=By.ID, value='password')
password.send_keys(PASSWORD)
time.sleep(5)
sign_in = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
time.sleep(5)