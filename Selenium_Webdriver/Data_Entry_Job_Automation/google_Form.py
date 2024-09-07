from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import requests


EMAIL = 'send.test02@gmail.com'
PASSWORD = '1357@asdf'

chrome_options = webdriver.ChromeOptions()

class Google_Form_Interaction:
    def __init__(self, url, address, price, link, result_url):
        self.link_list = link
        self.address_list = address
        self.price_list = price
        self.google_form_url = url
        self.google_form_result = result_url
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= self.chrome_options)
        self.complete_form()

    def complete_form(self):
        self.driver.get(self.google_form_url)
        sleep(2)

        for x in range(len(self.price_list)):
            self.address_input = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            self.price_input = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            self.link_input = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            self.submit = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            try:
                self.address_list[x]
                self.price_list[x]
                self.address_list[x]
            except IndexError:
                break
            else:
                self.address_input.send_keys(self.address_list[x])
                self.price_input.send_keys(self.price_list[x])
                self.link_input.send_keys(self.address_list[x])
            finally:
                self.submit.click()
                sleep(2)
                self.submit_new = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
                sleep(2)

