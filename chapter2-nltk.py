import nltk
from nltk import word_tokenize
from nltk.corpus import nps_chat
from nltk.corpus import gutenberg
from nltk.corpus import brown

chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print (chatroom[123])

emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print (emma)
print (emma.concordance("surprize"))

emma1 = nltk.Text(nltk.corpus.brown.words('cr03'))
print (emma1)



 	
for fileid in brown.fileids():
    num_chars = len(brown.raw(fileid))
    num_words = len(brown.words(fileid))
    num_sents = len(brown.sents(fileid))
    num_vocab = len(set(w.lower() for w in brown.words(fileid)))
    #print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
