import requests
import shutil
import globals as gl
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

class DownloaderUtil:

    def downloadImage(self, adUrl):
        driver = gl.DRIVER
        driver.get(adUrl)
        driver.execute_script("document.getElementsByClassName('AdPhoneButton_expandHolder__q6qYA')[0].click()")
        adPhoneNumber = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div[2]/section[1]/div[3]/section[2]/section/div[1]/button/div[1]/span')
        file = None
        try:
            file = open(gl.FILE_PATH, 'a')
            file.write(adPhoneNumber.text.replace(" ", "") + "\n")
        except:
            print("POSSIBLY HANDLE FAIL SCENARIO")
        finally:
            file.close()