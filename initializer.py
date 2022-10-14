import requests
import os
import constants as cnts
from time import sleep
from bs4 import BeautifulSoup

class Initializer:

    def getConstants(self):
        req = requests.get(cnts.HOME_URL).text
        soup = BeautifulSoup(req, 'lxml')
        categories = soup.find('div', class_=cnts.CATEGORIES_LIST, id=cnts.GOODS_CATEGORY).find_all('a')

        for c in categories:
            urlCategoryPart = c['href']
            parsed = urlCategoryPart.split('/')
            cnts.CATEGORIES.append(parsed[1])
            cnts.CATEGORY_IDS.append(parsed[3])

        for c in categories:
            cnts.CATEGORY = urlCategoryPart = c['href'].split('/')[2]
            break

    def createSaveDirectory(self):
        dir_path = os.getcwd()
        folderName = 'numbers'
        path = os.path.join(dir_path, folderName)
        if not os.path.exists(path):
            os.mkdir(path)