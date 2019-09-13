from Article import Article
from newsapi import NewsApiClient
import string
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize

articleUser = Article(input("Link: "))
articleUser.currentWebsiteIs()
articleUser.cleanText()
articleUser.getDict()
articleUser.getRelated()


articles = []

for x in range(len(articleUser.compareTo)):
    articles.append(Article(articleUser.compareTo[x]))
 