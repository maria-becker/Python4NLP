######Sentiment Analysis with Textblob and NLTK######

import textblob
import nltk

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


sentence = "I love this library"

#Sentiment Analysis with Textblob
sentiment1 = TextBlob(sentence, analyzer=NaiveBayesAnalyzer())
sentiment2 = TextBlob(sentence)
print ("Sentiment Textblob 1:", sentiment1.sentiment)
print ("Sentiment Textblob 2:", sentiment2.sentiment)


#Sentiment Analysis with NLTK
sia = SIA()
print ("Sentiment NLTK", sia.polarity_scores(sentence))
