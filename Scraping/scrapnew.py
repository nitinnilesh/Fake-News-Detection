#!/usr/bin/python3
import csv, os, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
listofcat = ['india.txt', 'politics.txt', 'society.txt', 'media.txt', 'socialmedia.txt', 'entertainment.txt', 'sports.txt', 'technology.txt']
category = ['INDIA', 'POLITICS', 'SOCIETY', 'MEDIA', 'SOCIALMEDIA', 'ENTERTAINMENT', 'SPORTS', 'TECHNOLOGY']
listoflist = []
for j in range(len(listofcat)):
    f = open(listofcat[j],"r")
    lines = f.readlines()
    for i in range(len(lines)):
        driver = webdriver.Firefox()
        driver.get(lines[i])
        # try:
        #     val = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/article/header/h1')))
        #     valbody = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/article/div[1]')))
        # except:
        #     pass
        # wait = WebDriverWait(self.driver, 10)
        # val = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/div/div/article/header/h1')))
        # val.click()
        # valbody = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/div/div/article/div[1]')))
        # valbody.click()
        val = driver.find_elements_by_xpath('/html/body/section/div/div/article/header/h1')
        valbody = driver.find_elements_by_xpath('/html/body/section/div/div/article/div[1]')
        # time.sleep()
        list = []
        for i in range(len(val)):
            list.append(val[i].text)
            list.append(valbody[i].text)
            list.append(category[j])
        listoflist.append(list)
        driver.close()
    # print (listoflist)
        with open('fakingnews_scrapr1.csv', "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['HEADING', 'BODY', 'CATEGORY'])
            for item in listoflist:
                # print (item)
                writer.writerow(item)
        csv_file.close()
