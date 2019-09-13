from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import sys
sys.path.append("/home/memreyagci/Desktop/HackYeah_2019")
import frequentlyUsedWords
import urllib.request
import detectNews

newsapi = NewsApiClient(api_key = '493f8ac4bc004885acb60e8c7db2f25c')

# Getting the news' link from the user
link_user = input("Paste your link here: ")

# Necessary information of the website of the link.
website_detected = detectNews.sourceFinder(link_user)

# Headline and content of the news
link_headline = ''
link_content = ''

# Getting source of the link
x = urllib.request.urlopen(link_user)
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


# Merging the words of the headline and the content into a string
link_words = link_headline + " " + link_content

# Will be deleted after testing if if headline and content can be gotten correctly. 
text_file = open("Output.txt", "w")
text_file.write(link_words)
text_file.close()

# Creating a list consists of words used in the news 5 or more times
most_used_words = frequentlyUsedWords.get_words(link_words)
print(most_used_words)
# Searching the news in different websites and printing them
for i in range(len(detectNews.url)):
	if website_detected["id"] != detectNews.url[list(detectNews.url)[i]]["id"]:
		print(newsapi.get_everything(q = most_used_words, sources = detectNews.url[list(detectNews.url)[i]]["id"], from_param='2019-09-11', to='2019-09-13'), "\n"
			)