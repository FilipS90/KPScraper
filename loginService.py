import constants as cnts
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginService:

    def login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(cnts.HOME_URL)
        loginBtn = driver.find_element(By.XPATH, '//*[@id="topNavBlue"]/div[1]/a[1]')
        driver.execute_script("arguments[0].click();", loginBtn)
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('goran.47.misic@gmail.com')
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('fichony123')
        loginBtn = driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()
        print('Sign in done')