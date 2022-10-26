import globals as gl
from selenium.webdriver.common.by import By

class SiteLoginService:

    def login(self):
        driver = gl.DRIVER
        driver.get(gl.HOME_URL)
        loginBtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div[1]/div[1]/section/div/div/ul/li[2]/button')
        driver.execute_script("arguments[0].click();", loginBtn)
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('goran.47.misic@gmail.com')
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('fichony123')
        loginBtn = driver.find_element(By.XPATH, '//*[@id="kp-portal"]/div/div/aside/div/div/div[2]/main/div[3]/form/button').click()
        print('Sign in done')