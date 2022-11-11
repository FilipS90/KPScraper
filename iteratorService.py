import requests
import globals as gl
import dlUtil as dlu
import random
from subprocess import call
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


class IteratorService:

    driver = None
    saveCounter = 0

    def __init__(self):
        self.driver = gl.DRIVER

    def interateOverCategories(self):
        downloader = dlu.DownloaderUtil()
        for idx, category in enumerate(gl.CATEGORIES):
            fullUrl = gl.HOME_URL + '/' + category + '/' + gl.CATEGORY + '/' + gl.CATEGORY_IDS[idx]
            self.driver.get(fullUrl)

            btn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[3]/div/div/div/div[2]/form/section/div/div[1]/div/section/section/div/span[2]/button')
            self.driver.execute_script("arguments[0].click();",btn)
            self.iterateAdCategory(downloader)

    def iterateAdCategory(self, downloader):
        while(True):
            adUrls = self.getAdUrlsFromCurrentPage(self.driver.current_url)
            for adUrl in adUrls:
                print('downloading ad -> ' + adUrl)
                downloader.downloadImage(gl.HOME_URL + adUrl)
                sleep(random.randint(3,10))
                self.changeVpnOrIncrement(self.saveCounter)
            self.changePageNumber()


    def getAdUrlsFromCurrentPage(self, currentUrl):
        soup = BeautifulSoup(requests.get(currentUrl).text, 'lxml')
        adUrlsArray = soup.find('div', class_='Grid_col-lg-10__tIdze Grid_col-xs__6oZvU Grid_col-sm__hxOHE Grid_col-md__1bRJZ').find_all('a', class_='Link_link__J4Qd8 Link_inherit___qXEP AdGoldHeader_goldHeader__t_ira')
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
            self.driver.get(currentPage + '&page=' + str(newPageNum))
            return

        forUrlsOtherThanFirstPage = currentPage.split('page=')
        self.driver.get(forUrlsOtherThanFirstPage[0] + 'page=' + str(newPageNum))
        

    def changeVpnOrIncrement(self, saveCounter):
        if saveCounter == 50:
            call('proton-script')
            saveCounter = 0
        else:
            saveCounter += 1
