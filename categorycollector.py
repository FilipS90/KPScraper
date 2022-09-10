import requests
import constants
from time import sleep
from bs4 import BeautifulSoup

class CategoryCollector:

    allCategories = []

    def collector(self):
        req = requests.get(constants.SITE_URL).text
        soup = BeautifulSoup(req, 'lxml')
        categories = soup.find('div', class_=constants.CATEGORIES_LIST, id=constants.GOODS_CATEGORY).find_all('a')

        for c in categories:
            full = constants.SITE_URL + c['href']
            print(full)


q = CategoryCollector()
q.collector()