from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import sys
sys.path.append("/home/memreyagci/Desktop/HackYeah_2019")
import frequentlyUsedWords
import urllib.request

newsapi = NewsApiClient(api_key = '493f8ac4bc004885acb60e8c7db2f25c')

# Getting the news' link from the user
link_user = input("Paste your link here: ")

# Headline and content of the news
link_headline = ''
link_content = ''

# Getting source of the link
x = urllib.request.urlopen(link_user)
soup = BeautifulSoup(x,'lxml')

# Getting the content headline
for h1_tag in soup.find_all(class_ = "story-body__h1"):
	link_headline += h1_tag.text

# Getting the content
content_find = soup.findAll(class_ = "story-body__inner")
for i in content_find:
	for p_tag in i.find_all('p'):
		link_headline += p_tag.text

# Merging the words of the headline and the content into a string
link_words = link_headline + " " + link_content

# Creating a list consists of words used in the news 5 or more times
most_used_words = frequentlyUsedWords.get_words(link_words)

# Searching the news (in the same website to check its accuracy)
find_news = newsapi.get_everything(q = most_used_words, sources = 'bbc-news', from_param='2019-08-20', to='2019-08-23')

# Printing what the module found
print(find_news)