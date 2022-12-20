import nltk
from nltk import word_tokenize


####make file ready for NLTK###
file = open("nyt.txt", "r")
file_contents = file.read()
tokenized_raw_text = nltk.word_tokenize (file_contents)
final_text = nltk.Text(tokenized_raw_text)

######investigate specific words in a file######

###count word frequencies
print ("Word frequency of x:", final_text.count("nature"))

###see words in context
print ("Concordance of nature:")
final_text.concordance("nature")

###see words that appear in similar contexts
print ("Words similar to x:")
final_text.similar("nature")

print ("Word frequency of catastrophe:", final_text.count("catastrophe"))

###see words in context
print ("Concordance of catastrophe:")
final_text.concordance("catastrophe")

###see words that appear in similar contexts
print ("Words similar to catastrophe:")
final_text.similar("catastrophe")
