import requests
import os
import globals as gl
import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Initializer:

    def setup(self):
        # self.connectToVpn()
        self.createFiles()
        self.getConstants()
        self.chromeDriverCreator()

    def getConstants(self):
        req = requests.get(gl.HOME_URL).text
        soup = BeautifulSoup(req, 'lxml')
        categories = soup.find('div', class_=gl.CATEGORIES_LIST_CLASS).find_all('a')

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

    def createFiles(self):
        dir_path = os.getcwd()
        fileName = 'phone-numbers'
        path = os.path.join(dir_path, fileName)
        if not os.path.exists(path):
            open(path, mode='a').close()
        gl.FILE_PATH = path
        indexFileName = 'vpn-arr-index'
        path = os.path.join(dir_path, indexFileName)
        if not os.path.exists(path):
            file = None
            try:
                file = open(path, mode='a')
                file.write('1')
            finally:
                file.close()


    def chromeDriverCreator(self):
        # browser_options = Options()
        # browser_options.headless = True
        gl.DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # options=browser_options

    def connectToVpn(self):
        bashCommand = 'protonvpn-cli connect CY#1'
        output = subprocess.check_output(bashCommand, shell=True)
        print(output)
