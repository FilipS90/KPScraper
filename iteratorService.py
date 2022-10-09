import requests
import constants as cnts
import dlUtil as dlu
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class IteratorService:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def interateOverCategories(self):
        downloader = dlu.DownloaderUtil()
        for idx, category in enumerate(cnts.CATEGORIES):
            fullUrl = cnts.HOME_URL + '/' + category + '/' + cnts.CATEGORY + '/' + cnts.CATEGORY_IDS[idx]
            self.driver.get(fullUrl)

            btn = self.driver.find_element(By.NAME, 'submit[search]')
            self.driver.execute_script("arguments[0].click();",btn)
            sleep(10)

            self.iterateOverSingleCategory(downloader)

    def iterateOverSingleCategory(self, downloader):
        while(True):
            adUrls = self.getAdUrls(self.driver.current_url)
            for adUrl in adUrls:
                print(adUrl.encode('utf-8'))
                sleep(7.5)
                print('downloading ad -> ' + adUrl)
                downloader.downloadImage(cnts.HOME_URL + adUrl)
            listbtn = self.driver.find_element(By.XPATH, "//ul[@class='pagesList clearfix']/li[last()]/a[last()]").click()


    def getAdUrls(self, currentUrl):
        soup = BeautifulSoup(requests.get(currentUrl).text, 'lxml')
        adUrlsArray = soup.find_all(class_='adName')
        resultArr = []
        for ad in adUrlsArray:
            if '?' in ad['href']:
                resultArr.append(ad['href'].split('?')[0])
            else:
                resultArr.append(ad['href'])
        return resultArr