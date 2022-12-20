import pandas as pd

##############################

# Reading in the co-occurrence matrix
bnc_table = pd.read_csv("data/bnc_table.csv", index_col=0)
#print(bnc_table)

# Reading in the WordSim353 pairs
with open("data/wordsim_similarity_goldstandard.txt", 'r') as f:
    lines = f.readlines()

    # a list of tuples, e.g. [('pair1word1', 'pair1word2'), ('pair2word1', 'pair2word2'), ...]
    pairs = [(x.split()[0].lower(), x.split()[1].lower()) for x in lines]
    #print(pairs)

    # the human annotated similarity score for each pair, in the order of the pairs list. The range of the scores is [0,10]
    human_scores = [float(x.split()[2]) for x in lines]
    #print(human_scores)

    # pairs and human scores combined, e.g. [(('pair1word1', 'pair1word2'), score1), (('pair2word1', 'pair2word2'), score2), ...]
    pairs_with_human_score = list(zip(pairs, human_scores))


##############################

# Implementing metrics
# If you don't know how to write functions, this and other resources might help: https://www.programiz.com/python-programming/function 

# Write a function, which takes two vectors and returns their euclidean distance.
# Do not use a preimplemented method (for example from scipy), though it is recommended to check you results.
def euclidean(u, v):
    '''your code here'''


# Write a function, which takes two vectors and returns their cosine similarity.
# Do not use a preimplemented method (for example from scipy), though it is recommended to check you results.
def cosine(u, v):
    '''your code here'''

##############################

# Use your functions to calculate euclidean distance and cosine similarity for two words aka vectors from the bnc_table
# Hint: You can use bnc_table.loc[word] to extract a row (aka the vector of the word)

'''your code here'''

##############################

# Compare your scores against the human annotated ones.
# You can find them already extracted as pairs, human_scores, and pairs_with_human_score

'''your code here'''

