from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import time

user_input="importance of database management"
url="https://www.quora.com/search?q="+user_input.replace(" ","%20")
browser=webdriver.Chrome()
browser.get(url)
time.sleep(2)
soup=BeautifulSoup(browser.page_source,"html.parser")
#print(soup.prettify())

for i in range(1):
    Class=f"q-box dom_annotate_question_answer_item_{i} qu-borderAll qu-borderRadius--small qu-borderColor--raised qu-boxShadow--small qu-mb--small qu-bg--raised"
    con = soup.find("div",class_=Class)
    name = soup.find("span", class_="q-box qu-userSelect--text").text
    print(name)

    more=browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/div')
    more.click()
    time.sleep(3)
    view_uv=browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div[2]/div[1]/div/div[1]/div/div[3]/div/span/span[4]/div')
    view_uv.click()
    time.sleep(10)
    upvotes=browser.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]').text
    print(upvotes)
    time.sleep(1)
    break
