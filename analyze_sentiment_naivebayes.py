import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import pandas as pd
from sklearn.metrics import accuracy_score
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import numpy as np


df = pd.read_csv("comments/train.csv", sep = "\t", encoding ='latin1')
sentiment_df = pd.DataFrame(data = df)
sentiment_df.columns = ["comment", "label"]
sentiment_df['comment'] = df['comment'].apply(nltk.word_tokenize)
stemmer = PorterStemmer()
sentiment_df['comment'] = sentiment_df['comment'].apply(lambda x: [stemmer.stem(y) for y in x])

# This converts the list of words into space-separated strings
sentiment_df['comment'] = sentiment_df['comment'].apply(lambda x: ' '.join(x))

count_vect = CountVectorizer()  
counts = count_vect.fit_transform(sentiment_df['comment'])  

# set that we'll train our classifier with
# training_set = sentiment_df.loc[:160,:]


X_train, X_test, y_train, y_test = train_test_split(counts, sentiment_df['label'], test_size=0.2, random_state=69)


model = MultinomialNB().fit(X_train, y_train)

predicted = model.predict(X_test)

print("accuracy is", np.mean(predicted == y_test))  



# set that we'll test against.
# testing_set = sentiment_df.loc[160:,:].tolist()

#classifier = nltk.NaiveBayesClassifier.train(training_set)




# # print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

# classifier.show_most_informative_features(15)