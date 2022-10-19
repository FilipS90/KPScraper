import requests
import globals as gl
import dlUtil as dlu
import initializer as i
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class IteratorService:

    driver = None

    def __init__(self):
        self.driver = gl.DRIVER

    def interateOverCategories(self):
        downloader = dlu.DownloaderUtil()
        for idx, category in enumerate(gl.CATEGORIES):
            fullUrl = gl.HOME_URL + '/' + category + '/' + gl.CATEGORY + '/' + gl.CATEGORY_IDS[idx]
            self.driver.get(fullUrl)

            btn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[3]/div/div/div/div[2]/form/section/div/div[1]/div/section/section/div/span[2]/button')
            self.driver.execute_script("arguments[0].click();",btn)
            self.iterateOverSingleCategory(downloader)

    def iterateOverSingleCategory(self, downloader):
        while(True):
            adUrls = self.getAdUrls(self.driver.current_url)
            for adUrl in adUrls:
                print(adUrl.encode('utf-8'))
                print('downloading ad -> ' + adUrl)
                sleep(3)
                downloader.downloadImage(gl.HOME_URL + adUrl)
            self.changePageNumber()


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

    def changePageNumber(self):
        currentPage = self.driver.current_url
        newPageNum = None
        if 'page' in currentPage[-6:]:
            newPageNum = int(currentPage[-1]) + 1
        else:
            newPageNum = 2
        self.driver.find_element(By.ID, 'goToPageInput').send_keys(str(newPageNum))
        nextPageBtn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div[2]/section[2]/form/section/div/span/button')
        self.driver.execute_script("arguments[0].click();", nextPageBtn)
