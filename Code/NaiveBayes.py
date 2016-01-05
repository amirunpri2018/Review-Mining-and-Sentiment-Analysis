import nltk
import csv
from datetime import date
import matplotlib.pyplot as plt
from nltk import *
import sklearn

documents = []
reviews = []

# Generating Trainset from Amazon  
with open('D:\Downloads\\Blu-amazon-review.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        documents.append((row[1],row[3]))
        
# Created a list of 2000 most frequent words in reviews
all_words = nltk.FreqDist(w.lower() for w in list(set(word_tokenize(str(documents)))))
wfeatures = list(all_words)[:2000]

# Document_feature function returns a featureset list of tuples containing two values
# a 0 or 1 value on the list of words of the review based on if it exists in the frequent words,
# and a 0 or 1 label based on negative or positive
def document_feature(document):
    document_words = set(document)
    features = {}
    for word in wfeatures:
        features['contains(%s)' % word] = (word in document_words)
    return features

# Applying document_feature on reviews and creating our feature set
featuresets = []
for i in range(len(documents)):
    a = document_feature(str.split(documents[i][0]))
#     print document_feature(str.split(documents[i][0]))
    featuresets.append((a,documents[i][1]))

# Dividing our featuresets into train and test
train_set, test_set = featuresets[:1000], featuresets[1001:1200]
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Print classifier accuracy
print(nltk.classify.accuracy(classifier, test_set))

# Print most important features in Naive Bayes prediction
classifier.show_most_informative_features(20)