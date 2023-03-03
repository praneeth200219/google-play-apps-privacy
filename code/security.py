#Code to collect security practices of each app

import pandas as pd
import re
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="C:/Users/praneeth/Downloads/chromedriver.exe", chrome_options=options)

df = pd.read_csv('review_kids_apps.csv')
k = df['app_name'].unique()
length = len(k)
print(length)
count = 0
for ele in k:
    print(count)
    count = count + 1
    url = "https://play.google.com/store/apps/datasafety?id=" + str(ele)
    driver.get(url)
    try:
        more_icon = driver.find_elements(By.XPATH, './/i[@class="google-material-icons VfPpkd-kBDsod tGvJLc"]')
        for ele in more_icon:
            ele.click()
    except:
        pass
    
    try:
        blocks = driver.find_elements(By.XPATH, './/div[@class="Mf2Txd"]')
        path = "Apps_Data_Safety/" + str(ele) + ".txt"
        preprocess(blocks,path)
    except:
        pass

def preprocess(blocks,path):
    file = open(path,"w")
    
    # 1. No data shared preprocessing
    part1 = blocks[0].text
    part1 = part1 + "\n\n"
    file.write(part1)
    
    # 2. Data Collected Preprocessing
    raw = blocks[1].text
    if "Personal info" in raw:
        raw = raw.replace("Personal info", "PersonalInfo")
    if "App info" in raw:
        raw = raw.replace("App info", "AppInfo")
    if "Financial info" in raw:
        raw = raw.replace("Financial info", "FinancialInfo")

    raw = raw.replace("info","\n")
    from io import StringIO
    s = StringIO(raw)
    arr = []
    element = 0
    for line in s:
        arr.append(line)
        if "expand_less" in line:
            arr[element-2] = "\n" + arr[element-2]
        element = element + 1


    for ele in arr:
        if "expand_less" in ele:
            continue
        else:
            file.write(str(ele))
    
    # 3. Security Practices
    part3 = blocks[2].text
    part3 = part3.replace("Security practices","\n\n\n" + "Security practices\n")
    p3 = StringIO(part3)
    for line in p3:
        file.write(line)
    file.close()
