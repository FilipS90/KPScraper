import requests
import globals as gl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://novi.kupujemprodajem.com/alati-i-orudja/pretraga?categoryId=969'
# xpath /html/body/div[1]/div/div[3]/div/div/div[2]/section[2]/form/section/div/input
driver.get(url)
driver.execute_script("document.evaluate('/html/body/div[1]/div/div[3]/div/div/div[2]/section[2]/ul/li[8]/a', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()")