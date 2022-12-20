import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

####make file ready for NLTK###
file = open("CNN7522.txt", "r")
file_contents = file.read()
tokenized_raw_text = nltk.word_tokenize (file_contents)
final_text = nltk.Text(tokenized_raw_text)

    
####printing stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

stops = set(stopwords.words('german'))
#print(stops)

stops = set(stopwords.words('english'))
#print(stops)

 
### stopword removal on an example sentence


### stopword removal on a file

import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
stop_words = set(stopwords.words('english'))

file = open("CNN7522.txt", "r")
line = file.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext.txt','a')
        appendFile.write(" "+r)
        appendFile.close()





