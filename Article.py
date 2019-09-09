from bs4 import BeautifulSoup
import urllib.request
import nltk
from textblob import TextBlob


class Source:
    def __init__(self,url,headerTag,bodyTag,):
        self.url = url
        self.headerTag = headerTag
        self.bodyTag = bodyTag
        
# Class that handles with detecting the website, getting headline & content, seperating them to words -excluding stop words, and deciding whether it is an opinion or a fact article.
class Article:
    def __init__(self, linkUser):
        self.linkUser = linkUser

    def webScrap(self):
        #things I need to do in this function :
         #Detect the web source (example : is it bbc/associated press/abc/al jazeera)
         #Assign variables to it
        bbc = Source('https://www.bbc.com/','story-body__h1','story-body__inner')
        ap = Source('https://apnews.com/','headLine','Article')
        abc = Source('https://abcnews.go.com/','article-header','article-copy')
        washPost = Source('https://www.washingtonpost.com/','topper-headline','article-body')
        websites = [bbc,ap,abc,washPost]
        currentWebsite = ''


        self.header = ' '
        self.textBody = ' '

        # Removing path of the 'linkUser'
        def findWebsite():
            from urllib.parse import urlparse
            parsed_uri = urlparse(self.linkUser)
            result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            return (result)
        
        # Getting content and headline
        def scrap():
            for website in websites:
                if website.url == findWebsite():
                    currentWebsite = website

            source = urllib.request.urlopen(self.linkUser)
            soup = BeautifulSoup(source,'lxml')

            headDiv = soup.find_all('div',attrs={'class': currentWebsite.headerTag})
            bodyDiv = soup.find_all('div',attrs={'class': currentWebsite.bodyTag})

            for x in headDiv:
                for head in x.find_all('h1'):
                    self.header += head.text
            
            for x in bodyDiv:
                for parag in x.find_all('p'):
                    self.textBody += parag.text + ' '

        scrap()
        
        # = soup.findAll('div',attrs={'class':})


    def cleanText(self):
        self.stopWords = ['or','a','an','the','and','i','we','you','he','she','it','about', 'above', 'across', 'after', 'against', 'along', 'among', 'around', 'at',
        'because of', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between',
        'beyond', 'but', 'by', 'concerning', 'despite', 'down', 'during', 'except', 'excepting',
        'for', 'from', 'in', 'in front of', 'inside', 'in spite of', 'instead of', 'into',
        'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past', 'regarding',
        'since', 'through', 'throughout', 'to', 'toward', 'under', 'underneath', 'until', 'up',
        'upon', 'up to', 'with', 'within', 'without', 'with regard to', 'with respect to', 'is', 'are', '-', 's', 'they',
        'were', 'had', "--", "was", "as", "told", "said", "no", "that", "re", "been", "but", "not", "would"]
        from nltk import tokenize
        from nltk.corpus import stopwords
        self.webScrap()


        self.wordList = tokenize.word_tokenize(self.textBody)
        for x in range(len(self.wordList)):
            self.wordList[x] = self.wordList[x].lower()
        self.sentenceList = tokenize.sent_tokenize(self.textBody)
        self.cleaned_List = []

        for i in range(len(self.wordList)):
            if self.wordList[i] != self.stopWords:
                self.cleaned_List.append(self.wordList[i])

        

    def opinion_fact_Check(self):
        self.isOpinion = False
        opinions = []
        facts = []
        for x in self.sentenceList:
            textBlob = TextBlob(x)
            if textBlob.sentiment.subjectivity > 0.5:
                opinions.append(x)
            if textBlob.sentiment.subjectivity < 0.5:
                facts.append(x)
        average = len(opinions) / len(facts)

        if average > 0.5:
            self.isOpinion = True
    
    #def topicModelling(self):
        
    #change the name
    #def mainAlgorithm(self):
        #Things to consider
         #Objectivity or subjectivity
         #Amount of equal unique words
         #Authors score
         #key words (maybe)
         #header
         #websites score
         #topic modelling results


article = Article(input("Please enter the link: "))

article.cleanText()
article.opinion_fact_Check()
print(article.isOpinion)



