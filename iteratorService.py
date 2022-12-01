import requests
import globals as gl
import dlUtil as dlu
import random
import os
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
        firstExecution = True
        startPage = None
        categoryId = None
        for idx, category in enumerate(gl.CATEGORIES):

            if firstExecution:
                vals = self.checkSavedProgress()
                startPage = vals.split('-')[1]
                categoryIdx = int(vals.split('-')[0])
                if categoryIdx > idx:
                    continue
                # https://novi.kupujemprodajem.com/alati-i-orudja/pretraga?category=alati-i-orudja&categoryId=969&page=3
                categoryName = gl.CATEGORIES[categoryIdx]
                fullUrl = gl.HOME_URL + '/' + categoryName + '/pretraga?category=' + categoryName + '&categoryId=' + gl.CATEGORY_IDS[categoryIdx] + '&page=' + startPage

                # PRETRAZI KAO DOLE CELU KATEGORIJU I ONDA KLIKNI NA STRANICU DO KOJE SI STIGAO
                # POSTO OVAKO BACA NA STARI SAJT

                self.driver.get(fullUrl)
                sleep(5) # sleep so above command loads entirely
                self.iterateAdCategory(downloader, startPage)
                firstExecution = False
                continue

            gl.CURRENT_CATEGORY_IDX = idx
            fullUrl = gl.HOME_URL + '/' + category + '/' + gl.CATEGORY + '/' + gl.CATEGORY_IDS[idx]
            self.driver.get(fullUrl)

            btn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[3]/div/div/div/div[2]/form/section/div/div[1]/div/section/section/div/span[2]/button')
            self.driver.execute_script("arguments[0].click();",btn)
            sleep(1) # sleep so above command loads entirely
            self.iterateAdCategory(downloader, startPage)

    def iterateAdCategory(self, downloader, startPage):
        currentAdPage = startPage
        maxAdPage = self.fetchMaxAdPage()
        while(True):
            adPageUrl = self.driver.current_url
            print(adPageUrl)
            adUrls = self.getAdUrlsFromCurrentPage(adPageUrl)
            self.saveProgress(currentAdPage)

            for adUrl in adUrls:
                print(adUrl)
                downloader.downloadImage(gl.HOME_URL + adUrl)
                sleep(random.randint(2,5)) # slow down execution, don't trigger prompt for too many requests
                self.changeVpnOrIncrement()

            if currentAdPage == maxAdPage:
                return
            currentAdPage = self.nextAdPage(adPageUrl)


    def getAdUrlsFromCurrentPage(self, currentUrl):
        soup = BeautifulSoup(requests.get(currentUrl).text, 'lxml')
        adUrlsArr = soup.find('div', class_='Grid_col-lg-10__tIdze Grid_col-xs__6oZvU Grid_col-sm__hxOHE Grid_col-md__1bRJZ').find_all('a', class_='Link_link__J4Qd8 Link_inherit___qXEP')
        resultArr = []
        for ad in adUrlsArr:
            if '?' in ad['href']:
                resultArr.append(ad['href'].split('?')[0])
            else:
                resultArr.append(ad['href'])
        return resultArr

    def nextAdPage(self, adPageUrl):
        print('--- new page ---')
        newPageNum = None
        if 'page' in adPageUrl[-6:]:
            newPageNum = int(adPageUrl[-1]) + 1
        else:
            newPageNum = 2
            self.driver.get(adPageUrl + '&page=' + str(newPageNum))
            return 2

        forUrlsOtherThanFirstPage = adPageUrl.split('page=')
        self.driver.get(forUrlsOtherThanFirstPage[0] + 'page=' + str(newPageNum))
        return newPageNum

    def fetchMaxAdPage(self):
        req = requests.get(self.driver.current_url).text
        soup = BeautifulSoup(req, 'lxml')
        maxPageStr = soup.find('ul', class_='Pagination_pagination__81Zkn').find_all('span', class_='Button_children__3mYJw')[5]
        return int(maxPageStr.text)  

    def changeVpnOrIncrement(self):
        if self.saveCounter == 50:
            call('proton-script')
            self.saveCounter = 0
        else:
            self.saveCounter += 1

    def checkSavedProgress(self):
        file = None
        val = None
        try:
            file = open('save-progress', 'r')
            val = file.read()
        except:
            val = '0-1'
            print('error in checkSavedProgress, starting from beginning..')
        finally:
            file.close()
        return val

    def saveProgress(self, currentAdPage):
        file = None
        try:
            file = open('save-progress', 'w')
            file.write(str(gl.CURRENT_CATEGORY_IDX) + '-' + str(currentAdPage))
        except Exception as e:
            print(e)
        finally:
            file.close()