from newsapi import NewsApiClient
import bs4 as bs
import urllib.request

newsapi = NewsApiClient(api_key='c3ef595ba6414146b09332ae73cdf0eb')


target = newsapi.get_everything(q='amazon-g7-fund',sources='bbc-news',from_param='2019-08-20', to='2019-08-23')


target_URL = target['articles'][0]['url']

source = urllib.request.urlopen(target_URL)

soup = bs.BeautifulSoup(source,'lxml')


target_DIV = soup.findAll('div',attrs={'class':'story-body__inner'})

print("---------------------------------------------------------------------")

target_STR = ' '

for i in target_DIV:
    for parag in i.find_all('p'):
        target_STR += parag.text

text_file = open('datacollection.txt','w')
text_file.write(target_STR)
text_file.close()