from newsapi import NewsApiClient
import bs4 as bs
import urllib.request

#API AND WEB SCRAPING THINGS

newsapi = NewsApiClient(api_key='c3ef595ba6414146b09332ae73cdf0eb')

target = newsapi.get_everything(q='amazon-g7-fund',sources='bbc-news',from_param='2019-08-20', to='2019-08-23')

target_URL = 'https://www.bbc.com/news/world-asia-china-49540751'

source = urllib.request.urlopen(target_URL)

soup = bs.BeautifulSoup(source,'lxml')

target_DIV = soup.findAll('div',attrs={'class':'story-body__inner'})

#initial String to gather all the text in 1 variable
target_STR = ' '

for i in target_DIV:
    for parag in i.find_all('p'):
        target_STR += parag.text

#save the text to an external file
'''
def saveToExternalFile(string,filename):
        text_file = open(filename,'w')
        text_file.write(string)
        text_file.close()
'''
#cleaning up the text for better analysis
stopWords = ['or','a','an','the','and','i','we','you','he','she','it','about', 'above', 'across', 'after', 'against', 'along', 'among', 'around', 'at',
  'because of', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between',
  'beyond', 'but', 'by', 'concerning', 'despite', 'down', 'during', 'except', 'excepting',
  'for', 'from', 'in', 'in front of', 'inside', 'in spite of', 'instead of', 'into',
  'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past', 'regarding',
  'since', 'through', 'throughout', 'to', 'toward', 'under', 'underneath', 'until', 'up',
  'upon', 'up to', 'with', 'within', 'without', 'with regard to', 'with respect to','mr','was','said','the','is','','has','that',
  'have','this','are','be','also','not','which','-','were','they','had']


def cleanUpText(stopWords,string):
        words = []
        splitText = string.split(' ')
        #converting the text into lower case
        for i in range(len(splitText)):
                splitText[i] = splitText[i].lower()
        #making sure no stop words in the string
        for word in splitText:
                if word not in stopWords:
                        words.append(word)
        return words


def getWordFreq(words):
        wordFreq = []
        #adding the frequencies to a list
        for i in range(len(words)):
               wordFreq.append(words.count(words[i]))
        return wordFreq



#pairing the words with their frequencies
def pairTwoLists(list1,list2):
        return tuple((zip(list1,list2)))

#remove duplicate results from mostRepeated

def removeDuplicates(arr):
        return list(set(arr))


def querifyString():
        queryStr = ''
        for i in range(len(most_Repeated)):
                if most_Repeated[i] != most_Repeated[-1]:
                        queryStr += most_Repeated[i][0] + '-'
                else:
                        queryStr += most_Repeated[i][0]
        return queryStr

#Final Variables
cleanedText = cleanUpText(stopWords,target_STR)
word_Count = pairTwoLists(cleanedText,getWordFreq(cleanedText))



#To access the counter variable in the pair
  #word_Count[i][j]   i represents the index of the entire tuple j represents the elements inside that tuple
most_Repeated = []

#TO_DO 
#turn this into a function that returns the top n repeated words
for i in range(len(word_Count)):
                if word_Count[i][1] >= 5:
                        most_Repeated.append(word_Count[i])


most_Repeated = removeDuplicates(most_Repeated)
print(most_Repeated)


toSearch = querifyString()

#trying to see if the most used words can get us the exact article
target2 = newsapi.get_everything(q=toSearch,sources='associated-press', from_param='2019-08-20', to='2019-08-23')
#print(target2['articles'])
#print("----------------------------------")
#print(target)

#it kinda works :)


