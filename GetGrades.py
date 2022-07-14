from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys

from time import  sleep
from bs4 import BeautifulSoup
import pandas as pd
import requests


#Thw OpenU login URL
WEBSEITE_URL = "https://sso.apps.openu.ac.il/login?T_PLACE=https://sheilta.apps.openu.ac.il/pls/dmyopt2/sheilta.main"

#Path for crhomedrive.exe file for windows add chromedriver'.exe'
PATH_FOR_DRIVER = "/Users/almogshtaigmann/Downloads/chromedriver"

#Student information:
USER_NAME = "shALMO4"
PASSWARD = "AlmogOpen98"
ID = "209401553"

driver = webdriver.Chrome(PATH_FOR_DRIVER)
driver.get(WEBSEITE_URL)

# Get element with tag name 'div'
element = driver.find_element(By.ID, 'p_user')
element.send_keys(USER_NAME)

element = driver.find_element(By.ID, 'p_sisma')
element.send_keys(PASSWARD)

element = driver.find_element(By.ID, 'p_mis_student')
element.send_keys(ID)

element.send_keys(Keys.ENTER)


sleep(7)

l = driver.find_element("xpath","//*[@class= 'spTable']/tbody/tr")
# to get the row count len method
print (len(l))
# to close the browser




