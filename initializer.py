import requests
import os
import globals as gl
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Initializer:

    def init(self):
        self.createSaveDirectory()
        self.getConstants()
        self.chromeDriverCreator()

    def getConstants(self):
        req = requests.get(gl.HOME_URL).text
        soup = BeautifulSoup(req, 'lxml')
        categories = soup.find('div', class_=gl.CATEGORIES_LIST).find_all('a')

        for c in categories:
            urlCategoryPart = c['href']
            if urlCategoryPart == '/poslovi' or urlCategoryPart == '/usluge':
                continue
            parsed = urlCategoryPart.split('/')
            gl.CATEGORIES.append(parsed[1])
            gl.CATEGORY_IDS.append(parsed[3])

        for c in categories:
            gl.CATEGORY = urlCategoryPart = c['href'].split('/')[2]
            break

    def createSaveDirectory(self):
        dir_path = os.getcwd()
        folderName = 'numbers'
        path = os.path.join(dir_path, folderName)
        if not os.path.exists(path):
            os.mkdir(path)

    def chromeDriverCreator(self):
        # browser_options = Options()
        # browser_options.headless = True
        # options=browser_options
        gl.DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()))