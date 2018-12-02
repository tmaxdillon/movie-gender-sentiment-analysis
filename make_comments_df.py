from urllib import request
from os import listdir
import pandas as pd
import numpy as np
import analyze_comments_tblob as tblob

PATH = "movie_comments"
ANALYZED_PATH = "labeled_comments"

def make_movie_dfs():
    final_df = pd.DataFrame(columns=['movie_id','sentiment_score','gender_diversity_score'])
    filenames2 = find_csv_filenames(PATH)
    for name in filenames2:
        # print(name)
        new_name = PATH+"/"+name
        df = pd.read_csv(new_name, encoding ='latin1')
        sentiment_df = pd.DataFrame(data = df)
        sentiment_df.columns = ["comment"]
        if not sentiment_df.empty:
            sentiment_df = tblob.analyze_comments(sentiment_df)

            if name.endswith('.csv'):
                name = name[:-4]
            
        #sentiment_df.to_csv(ANALYZED_PATH+"/"+name+"_sentiment.csv", encoding='latin1')
            #print(sentiment_df.head())
            #sentiment_score = sentiment_df[:,'tblob_label'].mean()
            sentiment_score = np.asarray(sentiment_df.iloc[:,1], dtype=np.float).mean()
            # print(name, sentiment_score)
            final_df = add_row(name, sentiment_score, final_df)
    return final_df

def find_csv_filenames(path_to_dir, suffix=".csv"):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

def add_row(movie_id,mean_score, final_df):
    df2 = pd.DataFrame([[movie_id, mean_score]], columns=['movie_id','sentiment_score'])
    final_df = final_df.append(df2, ignore_index=True)
    return final_df

final_df = make_movie_dfs()
print(final_df.head(100))