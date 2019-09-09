from Article import Article

articles = []

#for every result from the API create an Article object
for i in range(articles):
    articles[i] = Article(articles[i]['url'])
    articles[i].doThings()

article1 = Article('https://www.bbc.com/news/business-49625303')
article2 = Article('https://abcnews.go.com/Travel/wireStory/british-airways-grounds-flights-pilots-strike-65477999?cid=clicksource_4380645_null_headlines_hed')
article3 = Article('https://www.washingtonpost.com/business/2019/09/09/british-airways-grinds-halt-pilots-go-day-strike/')
article4 = Article('https://apnews.com/baaba9bbb7934b6f9da725c1b79825cf')
article1.cleanText()
article2.cleanText()
article3.cleanText()
article4.cleanText()


commonWords = []

for i in set(article1.cleaned_List):
    for j in set(article2.cleaned_List):
        for x in set(article3.cleaned_List):
            for y in set(article4.cleaned_List):
                if i == j == x == y:
                    commonWords.append(i)

#354 - 136 

print(len(set(article1.cleaned_List)))
print(len(set(article2.cleaned_List)))
print(len(set(article3.cleaned_List)))
print(len(set(article4.cleaned_List)))
print(commonWords)
print(len(commonWords))