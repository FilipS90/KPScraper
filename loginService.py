import constants as cnts
import initializer as intlzr
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class LoginService:

    def login(self):
        driver = cnts.DRIVER
        driver.get(cnts.HOME_URL)
        xButton = driver.find_element(By.XPATH, '//*[@id="bodyTag"]/div[9]/div/div[2]')
        driver.execute_script("arguments[0].click();",xButton)
        loginBtn = driver.find_element(By.XPATH, '//*[@id="topNavBlue"]/div[1]/a[1]')
        driver.execute_script("arguments[0].click();", loginBtn)
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('goran.47.misic@gmail.com')
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('fichony123')
        loginBtn = driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()
        print('Sign in done')