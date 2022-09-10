import requests
import shutil
import constants
from bs4 import BeautifulSoup

class DownloaderUtil:

    fileNum = 0
    soup = None

    def __init__(self, adUrl):
        self.soup = BeautifulSoup(requests.get(adUrl).text, 'lxml')


    def downloadImage(self):
        numberUrl = self.soup.find('div', class_='phone-number').find_all('img')[1]['src']
        url = constants.SITE_URL + numberUrl
        numImage = requests.get(url, stream = True)
        try:
            file = open('image' + str(self.fileNum) + '.png', 'wb')
            shutil.copyfileobj(numImage.raw, file)
        except:
            print("POSSIBLY HANDLE FAIL SCENARIO")
        finally:
            file.close()
        self.fileNum += 1