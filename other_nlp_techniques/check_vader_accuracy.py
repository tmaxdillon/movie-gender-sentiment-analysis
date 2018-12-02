import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import pandas as pd
from sklearn.metrics import accuracy_score


def vader_polarity(text):
    """ Transform the output to a binary 0/1 result """
    score = sid.polarity_scores(text)
    feature = nltk.sentiment.vader.SentiText(text)
    return 'pos' if score['pos'] > score['neg'] else 'neg'
  
df = pd.read_csv("comments/train.csv", sep = "\t", encoding ='latin1')
sentiment_df = pd.DataFrame(data = df)
sentiment_df.columns = ["comment", "label"]
sid = SentimentIntensityAnalyzer()

for index, row in sentiment_df.iterrows():
    stripped_whitespace = row[0].replace("\r", "")
    sentiment_df.at[index,'comment']=stripped_whitespace
    comment =  sentiment_df.at[index,'comment']
    vader_label = vader_polarity(comment)
    sentiment_df.at[index, 'vader_label']= vader_label
    
print(sentiment_df.head())
print ("accuracy is", accuracy_score(sentiment_df.loc[:,'label'].tolist(), sentiment_df.loc[:,'vader_label'].tolist()))