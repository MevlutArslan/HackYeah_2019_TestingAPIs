from Article import Article
from newsapi import NewsApiClient
import string
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize

articleUser = Article(input("Link: "))
articleUser.run()
articleUser.getRelated()

articles = []

for x in range(len(articleUser.compareTo)):
    articles.append(Article(articleUser.compareTo[x]))
 
for article in articles:
    article.run()

commonWords = []

for article in articles:
    for word in article.cleanText():
        if word in articleUser.cleanText():
            commonWords.append(word)

print(commonWords)
