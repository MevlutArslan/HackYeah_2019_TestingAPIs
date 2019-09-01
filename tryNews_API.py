from newsapi import NewsApiClient
import bs4 as bs
import urllib.request

newsapi = NewsApiClient(api_key='c3ef595ba6414146b09332ae73cdf0eb')


target = newsapi.get_everything(q='amazon-g7-fund',sources='bbc-news',from_param='2019-08-20', to='2019-08-23')


target_URL = 'https://www.bbc.com/news/world-asia-china-49540751'

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

#cleaning up the text for better analysis

stopWords = ['or','a','an','the','and','i','we','you','he','she','it','about', 'above', 'across', 'after', 'against', 'along', 'among', 'around', 'at',
  'because of', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between',
  'beyond', 'but', 'by', 'concerning', 'despite', 'down', 'during', 'except', 'excepting',
  'for', 'from', 'in', 'in front of', 'inside', 'in spite of', 'instead of', 'into',
  'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past', 'regarding',
  'since', 'through', 'throughout', 'to', 'toward', 'under', 'underneath', 'until', 'up',
  'upon', 'up to', 'with', 'within', 'without', 'with regard to', 'with respect to','mr','was','said','the','is','','has','that',
  'have','this','are','be','also','not','which','-','were','they','had']

clean_Text = target_STR.split(' ')

#converting the text into lower case
for i in range(len(clean_Text)):
        clean_Text[i] = clean_Text[i].lower()

print("-------------------------------------------------------------------------")


#The processs of pairing words with their frequencies in the text

words = []
wordFreq = []

#making sure no stop words in the string
for word in clean_Text:
        if word not in stopWords:
                words.append(word)
                 
#adding the frequencies to a list
for i in range(len(words)):
        wordFreq.append(words.count(words[i]))

#pairing the words with their frequencies
word_Count = tuple((zip(words,wordFreq)))


#To access the counter variable in the pair
  #word_Count[i][j]   i represents the index of the entire tuple j represents the elements inside that tuple
most_Repeated = []


for i in range(len(word_Count)):
                if word_Count[i][1] >= 5:
                        most_Repeated.append(word_Count[i])

print("-------------------------------------------------------------------------")



to_SEARCH = ""
#remove duplicate results from mostRepeated
most_Repeated = list(set(most_Repeated))

print(most_Repeated)

for i in range(len(most_Repeated)):
        if most_Repeated[i] != most_Repeated[-1]:
                to_SEARCH += most_Repeated[i][0] + '-'
        else:
                to_SEARCH += most_Repeated[i][0]

#trying to see if the most used words can get us the exact article
target2 = newsapi.get_everything(q=to_SEARCH,sources='associated-press', from_param='2019-08-20', to='2019-08-23')
print(target2['articles'])
#print("----------------------------------")
#print(target)

#it kinda works :)


