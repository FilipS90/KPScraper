import requests
import shutil
import globals as gl
from bs4 import BeautifulSoup

class DownloaderUtil:

    fileNum = 0

    def downloadImage(self, adUrl):
        file = None
        soup = BeautifulSoup(requests.get(adUrl).text, 'lxml')
        numberUrl = soup.find('div', class_='phone-number').find_all('img')[1]['src']
        url = gl.HOME_URL + numberUrl
        numImage = requests.get(url, stream = True)
        try:
            file = open('numbers/number_pngs' +'image' + str(self.fileNum) + '.png', 'wb')
            shutil.copyfileobj(numImage.raw, file)
            print('image saved')
        except:
            print("POSSIBLY HANDLE FAIL SCENARIO")
        finally:
            file.close()
        self.fileNum += 1