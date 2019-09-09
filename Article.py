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
        from nltk import tokenize
        from nltk.corpus import stopwords
        
        self.stopWords = ['-', '--', 'a', 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again', 'against', 'ain’t', 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', 'aren’t', 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'a’s', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beneath', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'bill', 'both', 'bottom', 'brief', 'but', 'by', 'call', 'came', 'can', 'cannot', 'cant', 'can’t', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes', 'con', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', 'couldnt', 'couldn’t', 'course', 'cry', 'currently', 'c’mon', 'c’s', 'de', 'definitely', 'describe', 'described', 'despite', 'detail', 'did', 'didn’t', 'different', 'do', 'does', 'doesn’t', 'doing', 'done', 'don’t', 'down', 'downwards', 'due', 'during', 'each', 'edu', 'eg', 'either', 'else', 'elsewhere', 'empty', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'excepting', 'far', 'few', 'fify', 'fill', 'find', 'fire', 'first', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'found', 'from', 'front', 'full', 'further', 'furthermore', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', 'hadn’t', 'happens', 'hardly', 'has', 'hasnt', 'hasn’t', 'have', 'haven’t', 'having', 'he', 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'here’s', 'hers', 'herself', 'he’s', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'hundred', 'i', 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead', 'interest', 'into', 'inward', 'is', 'isn’t', 'it', 'its', 'itself', 'it’d', 'it’ll', 'it’s', 'i’d', 'i’ll', 'i’m', 'i’ve', 'just', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'let’s', 'like', 'liked', 'likely', 'little', 'look', 'looking', 'looks', 'ltd', 'made', 'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'put', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'regard', 'regarding', 'regardless', 'regards', 'relatively', 'respect', 'respectively', 'right', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'several', 'shall', 'she', 'should', 'shouldn’t', 'show', 'side', 'since', 'sincere', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'spite', 'still', 'sub', 'such', 'sup', 'sure', 'system', 'take', 'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', 'thats', 'that’s', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'there’s', 'these', 'they', 'they’d', 'they’ll', 'they’re', 'they’ve', 'thick', 'thin', 'think', 'this', 'thorough', 'thoroughly', 'those', 'though', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'told', 'too', 'took', 'top', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 't’s', 'un', 'under', 'underneath', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'value', 'various', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', 'wasn’t', 'way', 'we', 'welcome', 'well', 'went', 'were', 'weren’t', 'we’d', 'we’ll', 'we’re', 'we’ve', 'what', 'whatever', 'what’s', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'where’s', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'who’s', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', 'won’t', 'would', 'wouldn’t', 'yes', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'you’d', 'you’ll', 'you’re', 'you’ve', 'zero']
        
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



