import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlJDZ0FQAQ', params={'hl':'en-ID', 'gl':'ID', 'ceid':'ID:en'})
soup = BeautifulSoup(html_doc.text, 'html.parser')

top_stories = soup.find(attrs={'class': 'D9SJMe'})
sections = top_stories.findAll(attrs={'class': 'PO9Zff Ccj79 kUVvS'})
news_list = []

s = 0
for s in range(len(sections)):
    sA = sections[s].findAll(attrs={'class': 'XBspb'})
    if(len(sA)>0):
        '''
        news_dict= {
            'title': sA.find('a', 'JtKRv').text
            # source=sA.findAll(attrs={'class': 'vr1PYe'}),
            # thumbnail=sA.findAll(attrs={'class': 'Quavad'}),
            # link=sA.findAll(attrs={'class': 'JtKRv'}).get('href')
        }
        news_list.append(news_dict)
        '''
        print(len(sA))
        print(sA[0].find('a', 'JtKRv').get('href'))
    '''
    sectionA.append(sections[s].findAll(attrs={'class': 'XBspb'}))
    sectionB.append(sections[s].findAll(attrs={'class': 'IBr9hb'}))
    sectionC.append(sections[s].findAll(attrs={'class': 'f9uzM'}))
    '''

print(news_list)