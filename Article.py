from bs4 import BeautifulSoup
import urllib.request
import nltk

class Article:
    def __init__(self, linkUser):
        self.linkUser = linkUser
    '''
    def webScrap():
        s
    '''

    def webScrap(self):

        newsSources = {
"BBC News": {"id" : "bbc-news", "url" : "bbc.co.uk", "headline_tag" : "story-body__h1", "headline_tag_2" : None, "content_tag" : "story-body__inner", "content_tag_2" : "p"},
"ABC News": {"id" : "abc-news", "url" : "abcnews.go.com", "headline_tag" : "article-header", "headline_tag_2" : "h1", "content_tag" : "article-copy", "content_tag_2" : "p"},
"The Wall Street Journal": {"id" : "the-wall-street-journal", "url" : "wsj.com", "headline_tag" : "bigTop__hed", "headline_tag_2" : None, "content_tag" : "wsj-snippet-body", "content_tag_2" : "p"}
}
        linkUser = self.linkUser

        website_detected = {}

        # A module that detects which website the link sent by the user belongs.
        # The parameter "link_user" is the link provided by user.
        for i in list(newsSources.keys()):
            if newsSources[i]["url"] in linkUser:
                website_detected = newsSources[i]
                break
        print(website_detected["content_tag_2"])

        # Headline and content of the news
        link_headline = ''
        link_content = ''

        # Getting source of the link
        x = urllib.request.urlopen(linkUser)
        soup = BeautifulSoup(x,'lxml')

        # Getting the content headline 
        for h_tag in soup.find_all(class_ = website_detected["headline_tag"]):
            if website_detected["headline_tag_2"] == None:
                link_headline += h_tag.text
            else:
                for h_tag_2 in h_tag.find_all(website_detected["headline_tag_2"]):
                    link_headline += h_tag_2.text

        # Getting the content 
        for c_tag in soup.find_all(class_ = website_detected["content_tag"]):
            if website_detected["content_tag_2"] == None:
                link_content += c_tag.text
            else:
                for c_tag_2 in c_tag.find_all(website_detected["content_tag_2"]):
                    link_content += c_tag_2.text

        link_words = link_headline + " " + link_content

        self.link_headline = link_headline
        self.link_content = link_content
        self.link_words = link_words

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

        self.wordList = tokenize.word_tokenize(self.link_words)
        for x in range(len(self.wordList)):
            self.wordList[x] = self.wordList[x].lower()
        self.sentenceList = tokenize.sent_tokenize(self.link_words)
        self.cleaned_List = [x for x in self.wordList if not x in self.stopWords]

        print(self.cleaned_List)



article = Article(input("Please enter the link: "))
article.webScrap()
article.cleanText()
