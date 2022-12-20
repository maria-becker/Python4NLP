import nltk
from nltk import word_tokenize


###prepare file###
file = open("cdu-NE.txt", "r")
file_contents = file.read()
tokenized_raw_text = nltk.word_tokenize (file_contents)
final_text = nltk.Text(tokenized_raw_text)


######investigate a document######

###show how many (different) words and punctuation symbold a file contains
#print ("Number of tokens: ", len(final_text))
#print ("Number of types: ", len(set(final_text)))
#print ("Lexical richness of the text:", len(set(final_text))/len(final_text))

###obtain a sorted list of vocabulary items
#print ("Sorted vocabulary list:", sorted(set(final_text)))

###generate similar text
#print ("Text generation:")
#final_text.generate()

###create a wordcloud of your file
import stylecloud
my_long_list = ["going", "news", "camera", "voiceover", "graphics", "graphic", "right", "said", "s", "new", "york", "times", "one", "like", "fox", "abc", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
my_long_list_2 = ["wikipedia", "Parlaments", "Deutscher","Bundestag", "Protokoll", "Plenarprotokoll", "Sitzung", "tageszeitung", "Ressort", "Süddeutsche", "Zeitung," "S", "ab", "aber", "abk.", "alle",
"allem", "allen", "aller", "alles", "allg.", "als", "also", "am", "zwischen",
"an", "ander", "andere", "anderem", "anderen", "anderer", "anderes",
"andern", "anders", "aber", "auch", "auf", "aus", "bei", "bes.",
"bez.", "bin", "bis", "bist", "bspw.", "da", "daß", "daher", "damit",
"dann", "das", "dass", "dasselbe", "dazu", "dein", "deine", "deinem",
"deinen", "deiner", "deines", "dem", "demselben", "den", "denn",
"denselben", "der", "derer", "derselbe", "derselben", "des",
"deshalb", "desselben", "dessen", "dich", "die", "dies", "diese",
"dieselbe", "dieselben", "diesem", "diesen", "dieser", "dieses",
"dir", "doch", "dort", "dt.", "du", "durch", "edv", "ehem.", "eigtl.",
"ein", "eine", "einem", "einen", "einer", "eines", "einig", "einige",
"einigem", "einigen", "einiger", "einiges", "einmal", "er", "es",
"etc.", "etwas", "euch", "euer", "eure", "eurem", "euren", "eurer",
"eures", "für", "ganz", "ganze", "ganzen", "ganzer", "ganzes",
"gegen", "ggf.", "hab", "habe", "haben", "hat", "hatten", "hier",
"hin", "hinter", "ich", "ihm", "ihn", "ihnen", "ihr", "ihre", "ihrem",
"ihren", "ihrer", "ihres", "im", "in", "indem", "ins", "ist", "ja",
"jede", "jedem", "jeden", "jeder", "jedes", "jene", "jenem", "jenen",
"jener", "jenes", "jetzt", "kein",
"keine", "keinem", "keinen", "keiner", "keines",  "mache",
"machst", "macht", "machte", "man", "manche", "manchem", "manchen",
"mancher", "manches", "mein", "meine", "meinem", "meinen", "meiner",
"meines", "mich", "mir", "mit", "nach", "nein", "nicht", "nichts",
"noch", "nun", "nur", "o.ã¤.", "ob", "oder", "o.g.", "ohne", "sein",
"seine", "seinem", "seinen", "seiner", "seines", "selbst", "sich", "sie", "sind", "so", "solche", "solchem", "solchen",
"solcher", "solches",  "sondern", "u.a.", "u.ä.", "u.g.",
"ugs.", "um", "und", "uns", "unser", "unter", "uvm.", "vgl.", "viel",
"vom", "von", "vor", "wãhrend", "wann", "warum", "was",
"weg", "weil", "weiter", "welche", "welchem", "welchen", "welcher",
"welches", "wenn", "wer", "wie", "wieder", "wir", "wo", "z.b.", "zu", "lesezeit", "minuten", 
"zum", "zur", "zwar", "werden", "wird", "für", "über", "seit", "uhr", "home", "u", "artikel", "cdu", "spd", "grüne", "afd", "linken", "linke", "csu", "grünen", "fdp", "sowie", "dabei"]
#modalverben: "kann", "können", "könnte", "konnte","sollte",
stylecloud.gen_stylecloud(file_path='test.txt', icon_name= "fas fa-cloud", custom_stopwords=my_long_list_2)
#custom_stopwords=my_long_list, 
#icon_name= "fas fa-apple-alt",

