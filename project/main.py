from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from time import sleep
from random import randint
import pandas as pd
from selenium.webdriver.support.ui import Select

executable_path = "C:\webdriver\chromedriver.exe"
try:
    driver = webdriver.Chrome(executable_path=executable_path)
except:
    driver = webdriver.Chrome()

url = 'https://aprtacitizen.epragathi.org/#!/regappstatus'
driver.get(url)
# slecect element by name 
select = driver.find_element_by_name('searchby')
driver.find_element_by_xpath("//select[@name='searchby']/option[text()='Permanent Registration Number']").click()
# select option form select tag
'''''
select.click()
select.send_keys('prNo')
select.send_keys(Keys.ENTER)
'''


sleep(5000)