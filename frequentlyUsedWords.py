# A module for listing the frequently used words
# in a string for the purpose of finding the same news
# on other news websites from the link sent by the user

# To add modules from different directory, add the code below to
# the .py file which this module is intended to be used:
# 
# import sys
# sys.path.append("location of the module goes here (with the quotes)")
#
# import frequentlyUsedWords
#

# 'content' indicates the string with the text 
def get_words (content):

	# Creates a list called 'words' by splitting the content string.
	# Making all the letters lower case prevents the module from
	# supposing the same words written with lower or upper cases
	# as different words.
	words = content.lower().split()

	# A dictionary for the purpose of counting the words with a
	# key-value relationship with the keys being words and the
	# the values being how many times they are used.
	word_dict = {}

	# Prevents differentation of the same words at the
	# beginning/middle of the sentence or at the end.
	special_characters_to_remove = """,?./'"!@#$&"""

	# Removing common words of preposition, conjunction, etc. from the result.
	words_to_remove = ['or','a','an','the','and','i','we','you','he','she','it','about', 'above', 'across', 'after', 'against', 'along', 'among', 'around', 'at',
'because of', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between',
'beyond', 'but', 'by', 'concerning', 'despite', 'down', 'during', 'except', 'excepting',
'for', 'from', 'in', 'in front of', 'inside', 'in spite of', 'instead of', 'into',
'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past', 'regarding',
'since', 'through', 'throughout', 'to', 'toward', 'under', 'underneath', 'until', 'up',
'upon', 'up to', 'with', 'within', 'without', 'with regard to', 'with respect to', 'is', 'are', '-', 's', 'they',
'were', 'had', "--", "was", "as", "told", "said", "no", "that", "re"]

	# Omitting the special characters from words in the 'words' list.
	for i in range(len(words)):
		for char in special_characters_to_remove:
			words[i] = words[i].replace(char, ' ')

	words = ' '.join(words).split()

	words_temp = []

	# Registering the words to a dictionary, excluding the words of
	# 'words_to_remove' list, with the count of 0.
	for i in words:
		if i not in words_to_remove:
			words_temp.append(i)
			word_dict[i] = 0

	# Regenerating words list without the words of 'word_to_remove'
	words = words_temp
	
	# The counting happens here
	for i in range(len(words)):
		for b in range(len(words)):
			if words[i] == words[b]:
				word_dict[words[b]] += 1
				words[b] = None

	# A string created since the 'q' parameter of newsapi requires a string
	word_str = ''
	
	# Checking if a word is used 5 or more times, and if yes, regitering
	# it to 'word_str'
	for i in range(len(word_dict)):
		if list(word_dict.values())[i] >= 5:
			word_str += list(word_dict.keys())[i] + " "

	return word_str
