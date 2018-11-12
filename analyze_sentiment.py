import make_comments_df as comments
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import pandas as pd
  
df = comments.make_dfs()
# print(df.head())

sentiment_df = pd.DataFrame(columns=['comment','neg','neu','pos','compound'])
# print(sentiment_df.head())

sid = SentimentIntensityAnalyzer()
for index, row in df.iterrows():
    stripped_whitespace = row[0].replace("\r", "")
    sentiment_df.at[index,'comment']=stripped_whitespace
    # print(sentence)
    ss = sid.polarity_scores(row[0])
    for k in ss:
        if k == "neg":
            sentiment_df.at[index, 'neg']=ss[k]
        elif k == "neu":
            sentiment_df.at[index, 'neu']=ss[k]
        elif k == "pos":
            sentiment_df.at[index, 'pos']=ss[k]
        else:
            sentiment_df.at[index, 'compound']=ss[k]
        # print('{0}: {1}, '.format(k, ss[k]), end='')
        # print()
print(sentiment_df.head())
print(sentiment_df.iloc[[6]])
sentiment_df.to_csv("sentiment_df_test.csv", encoding='latin1')