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
            sleep(1) # sleep so above command loads entirely
            self.iterateAdCategory(downloader)

    def iterateAdCategory(self, downloader):
        while(True):
            adPageUrl = self.driver.current_url
            adUrls = self.getAdUrlsFromCurrentPage(adPageUrl)
            print('printing ad urls')
            print(adUrls)
            for adUrl in adUrls:
                downloader.downloadImage(gl.HOME_URL + adUrl)
                sleep(random.randint(2,5))
                self.changeVpnOrIncrement(self.saveCounter)
            self.changePageNumber(adPageUrl)


    def getAdUrlsFromCurrentPage(self, currentUrl):
        soup = BeautifulSoup(requests.get(currentUrl).text, 'lxml')
        goldAdsUrlsArr = soup.find('div', class_='Grid_col-lg-10__tIdze Grid_col-xs__6oZvU Grid_col-sm__hxOHE Grid_col-md__1bRJZ').find_all('a', class_='Link_link__J4Qd8 Link_inherit___qXEP AdGoldHeader_goldHeader__t_ira')
        regularAdsUrlsArr = soup.find('div', class_='Grid_col-lg-10__tIdze Grid_col-xs__6oZvU Grid_col-sm__hxOHE Grid_col-md__1bRJZ').find_all('a', class_='Link_link__J4Qd8 Link_inherit___qXEP')
        adUrlsArr = goldAdsUrlsArr + regularAdsUrlsArr
        resultArr = []
        for ad in adUrlsArr:
            if '?' in ad['href']:
                resultArr.append(ad['href'].split('?')[0])
            else:
                resultArr.append(ad['href'])
        return resultArr

    def changePageNumber(self, adPageUrl):
        newPageNum = None
        if 'page' in adPageUrl[-6:]:
            newPageNum = int(adPageUrl[-1]) + 1
        else:
            newPageNum = 2
            print('first change')
            print(adPageUrl + '&page=' + str(newPageNum))
            self.driver.get(adPageUrl + '&page=' + str(newPageNum))
            return

        forUrlsOtherThanFirstPage = adPageUrl.split('page=')
        print('next page')
        print(forUrlsOtherThanFirstPage[0] + 'page=' + str(newPageNum))
        self.driver.get(forUrlsOtherThanFirstPage[0] + 'page=' + str(newPageNum))
        

    def changeVpnOrIncrement(self, saveCounter):
        if saveCounter == 50:
            call('proton-script')
            saveCounter = 0
        else:
            saveCounter += 1
