from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import random
import time
import re
from bs4 import BeautifulSoup
import requests
import json

driver = webdriver.Chrome()
driver.get("https://tabiturient.ru/")
time.sleep(2)
driver.execute_script("document.getElementById('limit').innerHTML = '460';")
WebDriverWait(driver, 0.8).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[5]/div/div'))).click()
time.sleep(5)
page = driver.page_source
with open("index2.html", "w", encoding="utf-8") as file_3:
    file_3.write(page)

# request передача браузера из селениума
'''s = requests.Session()
selenium_user_agent = driver.execute_script("return navigator.userAgent;")
s.headers.update({"user-agent": selenium_user_agent})
for cookie in driver.get_cookies():
    s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

response = s.get("https://tabiturient.ru/")

src = response.text

soup = BeautifulSoup(src, "lxml")
s = soup.find("span", id="limit")
print(s)
pars_name_stud = soup.find("div", id="resultdiv0").find_all("span", class_="font3")
name_stud = [i.text for i in pars_name_stud]
print(name_stud)'''