import nltk
import csv
from datetime import date
import matplotlib.pyplot as plt
import sklearn
import random

documents = []
reviews = []

# Generating Trainset from Amazon        
xtrain = []
ytrain = []
with open('D:\Downloads\\Blu-amazon-review.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        xtrain.append(row[1])
        ytrain.append(row[3])

# Created a list of 2000 most frequent words in reviews
wfeatures = list(nltk.FreqDist(w.lower() for w in list(set(nltk.word_tokenize(str(xtrain))))))[:2000]

# Twitter Tweets for prediction
with open('D:\Downloads\\b.tsv','rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')
    for row in csvreader:
        documents.append(row[2])


# Document_feature function returns a featureset list of
# a 0 or 1 value on the list of words of the review based on if it exists in the frequent words,
def document_feature(document):
    document_words = []
    document_words = set(document)
    features = []
    for word in wfeatures:
        if(word in document_words):
            features.extend('1')
        else:
            features.extend('0')
    return features

# Applying document_feature on reviews and creating our training set	
xt = []
for i in range(len(xtrain)):
    xt.append(document_feature(str.split(xtrain[i])))
    
# Initializing our svm classifier with a linear kernel and C='1'
clf = sklearn.svm.SVC(kernel='linear', C=1)

# Performing cross validation using svm classifier
score = sklearn.cross_validation.cross_val_score(clf, xt, ytrain, cv=10)
score.mean()
print(score)

# Creating classification report using SVM
predicted = sklearn.cross_validation.cross_val_predict(clf, xt, ytrain, cv=10)
sklearn.metrics.classification_report(ytrain, predicted)

# Fitting SVM on xt and ytrain
clf.fit(xt,ytrain)

# A manual test to check accuracy of our classifier
# Our classifier classified 5 out of 6 tweets correctly :)
tweets = []
tweets = ["camera is bad", "excellent", "camera is poor", "not waste", "awesome", "camera is great"]
tr =[]
for i in range(len(tweets)):
    tr.append(document_feature(str.split(tweets[i])))

a = clf.predict(tr)
print(a)


# documents containg twitter tweets
# Calculated our prediction of positive and negative public opinions
# on twitter tweets containing words related to camera
m = []
for x in documents :
    if("camera" in x.lower() or "picture" in x.lower() or "image" in x.lower() or "pixel" in x.lower() or "focus" in x.lower()):
        m.append(x)
print(m[3])
xt1 = []
for i in range(len(m)):
    xt1.append(document_feature(str.split(m[i])))
a = clf.predict(xt1)   

le = len(a)
sum = 0
for i in range(le):
    sum = sum + int(a[i])

print(sum)
print(le)
print(le-sum)


# Calculated our prediction of positive and negative public opinions
# on twitter tweets containing words related to storage
m = []
for x in documents :
    if("storage" in x.lower() or "size" in x.lower() or "capacity" in x.lower() or "gigabytes" in x.lower() or "bytes" in x.lower()):
        m.append(x)
print(len(m))
xt1 = []
for i in range(len(m)):
    xt1.append(document_feature(str.split(m[i])))
    
a = clf.predict(xt1)   
le = len(a)
sum = 0
for i in range(le):
    sum = sum + int(a[i])
print(sum)
print(le)
print(le-sum)    

# Calculated our prediction of positive and negative public opinions
# on twitter tweets containing words related to sound
m = []
for x in documents :
    if("sound" in x.lower() or "music" in x.lower() or "noise" in x.lower() or "voice" in x.lower() or "volume" in x.lower() or "audio" in x.lower()):
        m.append(x)
print(len(m))
xt1 = []
for i in range(len(m)):
    xt1.append(document_feature(str.split(m[i])))
    
a = clf.predict(xt1)   
le = len(a)
sum = 0
for i in range(le):
    sum = sum + int(a[i])
print(sum)
print(le)
print(le-sum)  


# Calculated our prediction of positive and negative public opinions
# on twitter tweets containing words related to speed
m = []
for x in documents :
    if("processor" in x.lower() or "speed" in x.lower() or "quadcore" in x.lower() or "ghz" in x.lower() or "ram" in x.lower() or "audio" in x.lower()):
        m.append(x)
print(len(m))
xt1 = []
for i in range(len(m)):
    xt1.append(document_feature(str.split(m[i])))
    
a = clf.predict(xt1)   
le = len(a)
sum = 0
for i in range(le):
    sum = sum + int(a[i])
print(sum)
print(le)
print(le-sum)  
#@C4ETech Thats a way to #confuse people with the 4gig RAM model of Zenfone 2
#@flipkartsupport Link: https://t.co/l0GkRfLGTrI bought a case from @amazonIN. They had delivery in Thiruvananthapuram

# Calculated our prediction of positive and negative public opinions
# on twitter tweets containing words related to price
m = []
for x in documents :
    if("money" in x.lower() or "cost" in x.lower() or "expenssive" in x.lower() or "cheap" in x.lower() or "price" in x.lower() or "value" in x.lower()  or "costly" in x.lower() or "budget" in x.lower() or "economical" in x.lower()):
        m.append(x)
print(len(m))
xt1 = []
for i in range(len(m)):
    xt1.append(document_feature(str.split(m[i])))
    
a = clf.predict(xt1)   
le = len(a)
sum = 0
for i in range(le):
    sum = sum + int(a[i])
print(sum)
print(le)
print(le-sum)  
#The Zenfone 2 is technically a budget phone but it doesn't feel like one. The design is it diff.. https://t.co/U0u0WHa2W1 #gadget
#Classified as 0 :Alternate ko sa iPhone 6, Asus Zenfone. I dunno why but the specs are good but price is too high
# Classified as 1 : @malabhargava mam, i personally have a zenfone 5 , its a beast in budget. Asus delivers raw power. Having good Service centers in kolkata.


# In[206]:

#print(m[:50])

m = []
for x in documents :
    if("light" in x.lower() or "weight" in x.lower() or "heavy" in x.lower() or "bulky" in x.lower() or "massive" in x.lower() or "large" in x.lower()  or "hefty" in x.lower() or "small" in x.lower() or "lightweight" in x.lower()):
        m.append(x)
print(len(m))
xt1 = []
for i in range(len(m)):
    xt1.append(document_feature(str.split(m[i])))
    
a = clf.predict(xt1)   
le = len(a)
sum = 0
for i in range(le):
    sum = sum + int(a[i])
print(sum)
print(le)
print(le-sum)  
print(m[100:120])
#q = "@malabhargava mam, i do have personally have a zenfone 5 , its a bad in budget. Asus delivers raw power. Having good Service centers in kolkata."

