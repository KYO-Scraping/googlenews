import os
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

html_doc = requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlJDZ0FQAQ', params={'hl':'en-ID', 'gl':'ID', 'ceid':'ID:en'})
soup = BeautifulSoup(html_doc.text, 'html.parser')

top_stories = soup.find(attrs={'class': 'D9SJMe'})
sections = top_stories.findAll(attrs={'class': 'PO9Zff Ccj79 kUVvS'})
base_link = 'https://news.google.com'
news_dict = {}
title = ''
link = ''
source = ''
thumbnail = ''
news_list = []

s = 0
for s in range(len(sections)):
    sA = sections[s].findAll(attrs={'class': 'XBspb'})
    sB = sections[s].findAll(attrs={'class': 'IBr9hb'})
    sC = sections[s].findAll(attrs={'class': 'UwIKyb'})

    if(len(sA)>0):
        # Section A
        title = sA[0].find('a', 'JtKRv').text # title
        link = str(base_link+sA[0].find('a', 'JtKRv').get('href')[1:]) # link
        source = sA[0].find('div', 'vr1PYe').text  # source
        try:
            thumbnail = sA[0].find(attrs={'class': 'Quavad'}).get('src')  # thumbnail
        except:
            thumbnail = 'No Thumbnail'
        news_dict = {
            'title' : title,
            'link' : link,
            'source' : source,
            'thumbnail' : thumbnail
        }
        news_list.append(news_dict)
    else:
        # Section B
        title = sB[0].find('a', 'gPFEn').text  # title
        link = str(base_link+sB[0].find('a', 'gPFEn').get('href')[1:])  # link
        source = sB[0].find('div', 'vr1PYe').text  # source
        try:
            thumbnail = sB[0].find(attrs={'class': 'Quavad'}).get('src')  # thumbnail
        except:
            thumbnail = 'No Thumbnail'
        news_dict = {
            'title': title,
            'link': link,
            'source': source,
            'thumbnail': thumbnail
        }
        news_list.append(news_dict)

        # Section C
        for c in range(len(sC)):
            title = sC[c].find('a', 'gPFEn').text  # title
            link = str(base_link+sC[c].find('a', 'gPFEn').get('href')[1:])  # link
            source = sC[c].find('div', 'vr1PYe').text  # source
            thumbnail = 'No Thumbnail'
            news_dict = {
                'title': title,
                'link': link,
                'source': source,
                'thumbnail': thumbnail
            }
            news_list.append(news_dict)

# Create JSON File
try:
    os.mkdir('json_result')
except FileExistsError:
    pass

with open('json_result/job_list.json', 'w+') as json_data:
    json.dump(news_list, json_data)

print('JSON Created')

# Create CSV and XLSX File
df = pd.DataFrame(news_list)
df.to_csv('googlenews_data.csv', index=False)
df.to_excel('googlenews_data.xlsx', index=False)
print('CSV and XLSX Created')
