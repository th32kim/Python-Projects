from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num = driver.find_element(by=By.LINK_TEXT, value='//*[@id="articlecount"]/a[1]')
# num.click()

# search = driver.find_element(by=By.NAME, value = 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

driver.get('http://secure-retreat-92358.herokuapp.com')

def input(value, text):
    value.send_keys(text)


def sign_up():
    First_Name = driver.find_element(by=By.NAME, value='fName')
    input(First_Name, 'Richard')
    Last_Name = driver.find_element(by=By.NAME, value='lName')
    input(Last_Name,'Kim')
    email = driver.find_element(by=By.NAME, value='email')
    input(email,'richard8851@gmail.com')
    sign_up = driver.find_element(by=By.XPATH, value='/html/body/form/button')
    sign_up.click()

sign_up()


