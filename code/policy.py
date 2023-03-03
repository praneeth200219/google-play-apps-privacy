#code to scrape the privacy

import pandas as pd
import re
import sys
import os
import json
import requests

from bs4 import BeautifulSoup

df = pd.read_csv('review_kids_apps_policy.csv')
ls_privacy_url = df['privacy_url'].unique().tolist()
ls_privacy_url.remove('NotFound')

with open('app_privacyurl.json', 'r') as j:
     dict_app_privacyurl = json.loads(j.read())
     
dict_url_app = {}
for app in dict_app_privacyurl:
    url = dict_app_privacyurl[app]
    dict_url_app[url] = app

def insert_newlines(string, every=120):
    c = 0
    final_str = ''
    if len(string) > every:
        words = string.split(' ')
        for word in words:
            c += len(word) + 1
            if c > every:
                c = len(word) + 1
                final_str += '\n' + word + ' '
            else:
                final_str += word + ' '            
    else:
        final_str = string    
    return final_str
  
ls_failed_to_retrieve = []
for idx, url in enumerate(ls_privacy_url[14:]):    
    app = dict_url_app[url]
    dst_fn = os.path.join('D:\playstore_data\policy data',app + '.txt' )
    print(app, url)
    text = []
    try:
        r = requests.get(url)        
        if str(r) == '<Response [200]>':
            soup = BeautifulSoup(r.content)
            with open(dst_fn, "w", encoding='utf-8') as text_file:            
                text_file.write("App Name: "+app+"\n\n")
                text_file.write("Privacy URL: "+url+"\n\n")
                text_file.write("Data Crawled: True \n\n")
                for item in soup.findAll('p'):
                    line = item.text
                    line = line.strip()
                    line = insert_newlines(line)
                    text_file.write(line+"\n\n")
        else:
            with open(dst_fn, "w", encoding='utf-8') as text_file:
                text_file.write("App Name: "+app+"\n\n")
                text_file.write("Privacy URL: "+url+"\n\n")
                text_file.write("Data Crawled: False \n\n")
                ls_failed_to_retrieve.append(url)

    except: 
        print('Failed')

for idx, url in enumerate(ls_privacy_url):    
    app = dict_url_app[url]
    dst_fn = os.path.join('D:\playstore_data\policy data',app + '.txt' )
    with open(dst_fn, "r", encoding='utf-8') as text_file:
        for line in text_file:
            if ('Data Crawled' in line) and( line[14:19]=='False'):
                print(app, url)
                break

for idx, url in enumerate(ls_failed_to_retrieve):    
    app = dict_url_app[url]
    dst_fn = os.path.join('D:\playstore_data\policy data',app + '.txt' )
    print(app, url)
    r = requests.get(url)       
    print(str(r))

ls_returned_empty = []
for idx, url in enumerate(ls_privacy_url):    
    c = 0
    count_start = False
    main_str = ''
    app = dict_url_app[url]
    dst_fn = os.path.join('D:\playstore_data\policy data',app + '.txt' )
    with open(dst_fn, "r", encoding='utf-8') as text_file:
        for idx, line in enumerate(text_file):
            if ('Data Crawled' in line):
                count_start = True
                continue
            if count_start:                
                c += len(line.strip())
                main_str += line.strip()
    if c == 0:
        print(main_str)
        print(app, url, c)
