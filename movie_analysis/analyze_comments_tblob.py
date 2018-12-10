"""This module analyzes the sentiment of a comment usign TextBlob it converts the
polarity score to a binary result: 1 if the polarity score is greater than or equal
to 0 (positive) or 0 if less than 0 (negative)
"""

from textblob import TextBlob

def analyze_comments(sentiment_df):
    """This function iterates through the row of a dataframe
    and analyzes the comment at each row and adds a sentiment
    score value next to each comment
    """

    for index, row in sentiment_df.iterrows():
        stripped_whitespace = row[0].replace("\r", "")
        sentiment_df.at[index, 'comment'] = stripped_whitespace
        comment = sentiment_df.at[index, 'comment']
        blob = TextBlob(comment)
        if blob.sentiment.polarity >= 0:
            sentiment_df.at[index, 'tblob_label'] = '1'
        else:
            sentiment_df.at[index, 'tblob_label'] = '0'
    return sentiment_df
