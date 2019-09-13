from bs4 import BeautifulSoup
import urllib.request
import nltk
from textblob import TextBlob
import re
import string
import datetime
from nltk import tokenize
from newsapi import NewsApiClient


# Class that handles with detecting the website, getting headline & content, seperating them to words -excluding stop words, and deciding whether it is an opinion or a fact article.
class Article:
    def __init__(self, urls):
        self.urls = urls
        self.websites = {
        "BBC News": {"id" : "bbc-news", "url" : "bbc.co.uk", "headline_tag" : "story-body__h1", "headline_tag_2" : None, "content_tag" : "story-body__inner", "content_tag_2" : "p", "date_tag_type" : "attribute", "date_tag" : "div", "date_tag_2": "data-datetime", "date_format": "%d %B %Y"},
        "ABC News": {"id" : "abc-news", "url" : "abcnews.go.com", "headline_tag" : "article-header", "headline_tag_2" : "h1", "content_tag" : "article-copy", "content_tag_2" : "p", "date_tag_type" : "no-attribute", "date_tag": "timestamp", "date_tag_2": None, "date_format": "%b %d, %Y, %I:%M %p ET"},
        "The Washington Post": {"id" : "the-washington-post", "url" : "washingtonpost.com", "headline_tag" : "topper-headline", "headline_tag_2" : None, "content_tag" : "article-body", "content_tag_2" : "p", "date_tag_type" : "attribute", "date_tag": "span", "date_tag_2": "content", "date_format": "%Y-%m-%dT%I:%M-500"},
        "AP News": {"id" : "associated-press", "url" : "apnews.com", "headline_tag" : "headline", "headline_tag_2" : None, "content_tag" : "Article", "content_tag_2" : "p", "date_tag_type" : "attribute", "date_tag": "span", "date_tag_2": "data-source", "date_format": "%Y-%m-%dT%H:%M:%SZ"}
        }


    def currentWebsiteIs(self):
        self.currentWebsite = ''

        for website in list(self.websites.keys()):
            if self.websites[website]["url"] in self.urls:
                self.currentWebsite = self.websites[website]

    # Getting content and headline
    def webScrap(self):

        self.header = ''
        self.textBody = ''
        self.articleDate = ''

        source = urllib.request.urlopen(self.urls)
        soup = BeautifulSoup(source,'lxml')

        # Getting the content headline 
        for h_tag in soup.find_all(class_ = self.currentWebsite["headline_tag"]):
            if self.currentWebsite["headline_tag_2"] == None:
                self.header += h_tag.text
            else:
                for h_tag_2 in h_tag.find_all(self.currentWebsite["headline_tag_2"]):
                    self.header += h_tag_2.text

        #Getting the content 
        for c_tag in soup.find_all(class_ = self.currentWebsite["content_tag"]):
            if self.currentWebsite["content_tag_2"] == None:
                self.textBody += c_tag.text
            else:
                for c_tag_2 in c_tag.find_all(self.currentWebsite["content_tag_2"]):
                    self.textBody += c_tag_2.text

        #Getting the date
        if self.currentWebsite["date_tag_type"] == "attribute":
            for i in soup.findAll(self.currentWebsite["date_tag"]):
                if i.has_attr(self.currentWebsite["date_tag_2"]):
                    self.articleDate = i[self.currentWebsite["date_tag_2"]]
                    break
        elif self.currentWebsite["date_tag_type"] == "no-attribute":
            for d_tag in soup.find_all(class_ = self.currentWebsite["date_tag"]):
                if self.currentWebsite["date_tag_2"] == None:
                    self.articleDate += d_tag.text
                    break
                else:
                    for d_tag_2 in d_tag.find_all(class_ = self.currentWebsite["date_tag_2"]):
                        self.articleDate += d_tag_2.text
                        break

        if self.currentWebsite["id"] == "abc-news":
            self.articleDate = self.articleDate[-24:]

        self.articleDate = datetime.datetime.strptime(self.articleDate, self.currentWebsite["date_format"]).date()

    def cleanText(self):
        self.stopWords = ['’',',','.','-', '--', 'a', 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again', 'against', 'ain’t', 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', 'aren’t', 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'a’s', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beneath', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'bill', 'both', 'bottom', 'brief', 'but', 'by', 'call', 'came', 'can', 'cannot', 'cant', 'can’t', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes', 'con', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', 'couldnt', 'couldn’t', 'course', 'cry', 'currently', 'c’mon', 'c’s', 'de', 'definitely', 'describe', 'described', 'despite', 'detail', 'did', 'didn’t', 'different', 'do', 'does', 'doesn’t', 'doing', 'done', 'don’t', 'down', 'downwards', 'due', 'during', 'each', 'edu', 'eg', 'either', 'else', 'elsewhere', 'empty', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'excepting', 'far', 'few', 'fify', 'fill', 'find', 'fire', 'first', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'found', 'from', 'front', 'full', 'further', 'furthermore', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', 'hadn’t', 'happens', 'hardly', 'has', 'hasnt', 'hasn’t', 'have', 'haven’t', 'having', 'he', 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'here’s', 'hers', 'herself', 'he’s', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'hundred', 'i', 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead', 'interest', 'into', 'inward', 'is', 'isn’t', 'it', 'its', 'itself', 'it’d', 'it’ll', 'it’s', 'i’d', 'i’ll', 'i’m', 'i’ve', 'just', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'let’s', 'like', 'liked', 'likely', 'little', 'look', 'looking', 'looks', 'ltd', 'made', 'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'put', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'regard', 'regarding', 'regardless', 'regards', 'relatively', 'respect', 'respectively', 'right', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'several', 'shall', 'she', 'should', 'shouldn’t', 'show', 'side', 'since', 'sincere', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'spite', 'still', 'sub', 'such', 'sup', 'sure', 'system', 'take', 'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', 'thats', 'that’s', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'there’s', 'these', 'they', 'they’d', 'they’ll', 'they’re', 'they’ve', 'thick', 'thin', 'think', 'this', 'thorough', 'thoroughly', 'those', 'though', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'told', 'too', 'took', 'top', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 't’s', 'un', 'under', 'underneath', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'value', 'various', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', 'wasn’t', 'way', 'we', 'welcome', 'well', 'went', 'were', 'weren’t', 'we’d', 'we’ll', 'we’re', 'we’ve', 'what', 'whatever', 'what’s', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'where’s', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'who’s', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', 'won’t', 'would', 'wouldn’t', 'yes', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'you’d', 'you’ll', 'you’re', 'you’ve', 'zero']
        self.webScrap()
        self.textBody = tokenize.word_tokenize(self.textBody)
        for x in range(len(self.textBody)):
            self.textBody[x] = self.textBody[x].lower()

        #self.sentenceList = tokenize.sent_tokenize(self.textBody)

        self.cleaned_List = [x for x in self.textBody if not x in self.stopWords]
        newWords = []
        for x in self.cleaned_List:
            newWords.append(''.join(c for c in x if c not in string.punctuation))
        self.cleaned_List = newWords

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
        average = (len(opinions) + len(facts)) / 2
        if average > 0.5:
            self.isOpinion = True
    
    def getRelated(self):
        articles = []

        newsapi = NewsApiClient(api_key = '493f8ac4bc004885acb60e8c7db2f25c')

        result = (newsapi.get_everything(
                q = self.word_str,
                sources = "bbc-news, abc-news, the-washington-post, associated-press",
                from_param = str(self.articleDate),
                to = str(self.articleDate + datetime.timedelta(days = 2))) , "\n\n\n")

        self.compareTo = []
        for x in range(len(result[0])):
            self.compareTo.append(result[0]["articles"][x]["url"])


    #generate document term matrix
    def generateDTM(self):
        import pandas as pd
        from collections import Counter
        #As rows we will generate an ID of 9 chars(Like a primary key)
        #As columns we will have unique words
        frequencies = Counter(self.cleaned_List)

        data = {
            frequencies:self.urls
        }
        self.DTM = pd.DataFrame(data)
        #DTM.to_csv('dTM.csv')

    def getDict(self):
        words = self.cleaned_List
        words_temp = []
        word_dict = {}

        # Registering the words to a dictionary with the count of 0.
        for i in words:
                word_dict[i] = 0

        # Regenerating words list without the words of 'word_to_remove'
        words_temp = words
        
        # The counting happens here
        for i in range(len(words)):
            for b in range(len(words)):
                if words[i] == words[b]:
                    word_dict[words[b]] += 1
                    words[b] = None

        words = words_temp

        # A string created since the 'q' parameter of newsapi requires a string
        self.word_str = ''
        
        # Checking if a word is used 5 or more times, and if yes, registering it to 'word_str'
        for i in range(len(word_dict)):
            if list(word_dict.values())[i] >= 5:
                self.word_str += list(word_dict.keys())[i] + " "


        self.header = tokenize.word_tokenize(self.header)
        for x in range(len(self.header)):
            self.header[x] = self.header[x].lower()
        self.cleaned_headline = [x for x in self.header if not x in self.stopWords]
        for x in self.cleaned_headline:
            self.word_str += x + " "


    def __str__(self):
        return self.urls

    def run(self):
        self.currentWebsiteIs()
        self.cleanText()
        self.getDict()