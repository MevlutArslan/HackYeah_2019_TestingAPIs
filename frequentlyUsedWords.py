# A module for listing the frequently used words
# in a string for the purpose of finding the same news
# on other news websites from the link sent by the user

# To add modules from different directory, add the code below to
# the .py file which this module is intended to be used:
# 
# import sys
# sys.path.append("location of the module goes here (with the quotes)")
#
# import word_counter
#

# 'content' indicates the string with the text
# and 'number_of_words' is how many of them user wants
# to be listed.
def get_words (content, number_of_words):

	# Creates a list called 'words' by splitting the content string.
	# Making all the letters lower case prevents the module from
	# supposing the same words written with lower or upper cases
	# as different words.
	words = content.lower().split()

	# A dictionary for the purpose of counting the words with a
	# key-value relationship with the keys being words and the
	# the values being how many times they are used.
	word_dict = {}

	# Prevents differentation of same the words at the
	# beginning/middle of the sentence or at the end.
	special_characters_to_remove = ".,?/'\"!@#$&"

	# Omitting the special characters from words in the 'words' list.
	for i in range(len(words)):
		for char in special_characters_to_remove:
			words[i] = words[i].replace(char, '')

	# Registering the words to a dictionary with the count of 0.
	for i in range(len(words)):
		word_dict[words[i]] = 0
	
	# The counting happens here
	for i in range(len(words)):
		for b in range(len(words)):
			if words[i] == words[b]:
				word_dict[words[i]] += 1
				words[i] = None


	a = 0

	# Printing the words with the amount user wants.
	for i in sorted (word_dict):
		if a < number_of_words:
			print(i, ":", word_dict[i], end = "\n")
			a += 1
		else:
			break
