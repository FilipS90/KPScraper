import requests
import constants
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

req = requests.get(constants.SITE_URL).text
soup = BeautifulSoup(req, 'lxml')

categories = soup.find('div', class_=constants.CATEGORIES_LIST, id=constants.GOODS_CATEGORY).find_all('a')
full = None

for c in categories:
    full = constants.SITE_URL + c['href']
    print(full)
    break

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(full)
sleep(3)
btn = driver.find_element(By.NAME, 'submit[search]')
driver.execute_script("arguments[0].click();",btn)

while(True):
    listbtn = driver.find_element(By.XPATH, "//ul[@class='pagesList clearfix']/li[last()]/a[last()]").click()
    print(driver.current_url)
    sleep(3)