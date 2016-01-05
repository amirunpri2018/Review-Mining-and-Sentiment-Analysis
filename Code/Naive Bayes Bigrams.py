import nltk
import csv
from datetime import date
import matplotlib.pyplot as plt
from nltk import *
from nltk.corpus import stopwords

documents = []
reviews = []

# Generating Trainset from Amazon  
with open("C:/Users/AshutoshBhargave/Desktop/Courses/Social Media Mining/Project/Blu-amazon-review.csv","rt") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        documents.append((row[0],row[3]))

exc = ["!","@","(",")",".",",","\\\\","\\'"]
all_words = nltk.FreqDist(w.lower() for w in list(set(word_tokenize(str(documents)))))
wfeatures = list(all_words)[:4000]

stopwords = nltk.corpus.stopwords.words('english')
exc = ["!","@","(",")","4g","internet", "4g internet"]
all_bigrams = nltk.FreqDist(" ".join(w).lower() for w in list(nltk.bigrams((word_tokenize(str(documents))))))# if " 

# Document_feature function returns a featureset list of tuples containing two values
# a 0 or 1 value on the list of words of the review based on if it exists in the frequent words,
# and a 0 or 1 label based on negative or positive
def document_feature(document):
    document_words = set(document)
    features = {}
    for word in wfeatures:
        features['contains(%s)' % word] = (word in document_words)
    return features

# Function for creating bigram_features
def bigram_feature(document):
    bigram_words = []
    for item in nltk.bigrams((word_tokenize(str(document)))):
           bigram_words.append(" ".join(item))
    bigram_words = set(bigram_words)
    bigram_features = {}
    for word in bigram_feature_words:
        bigram_features['contains(%s)' % word] = (word in bigram_words)
    return bigram_features

# Creating feature sets
featuresets = []
q = []
for i in range(len(documents)):
    a = document_feature(str.split(documents[i][0]))
    b = bigram_feature(str.split(documents[i][0]))
    b.update(a)
    featuresets.append((b,documents[i][1]))

# Dividing our featuresets into train and test
train_set, test_set = featuresets[:2000], featuresets[2051:2500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Print classifier accuracy and most important features
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(50)
