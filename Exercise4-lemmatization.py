import spacy

###prepare file###
file = open("CNN7522.txt", "r")
file_contents = file.read()

nlp = spacy.load('en_core_web_sm')
doc = nlp(file_contents)

######Lemmatization######
for token in doc:
    print("Token:", token, ";", "Lemma:", token.lemma_)
    #print(token.lemma_)
