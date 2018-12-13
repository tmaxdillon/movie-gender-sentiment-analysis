"""This module retrieves the trailer URLs and extracts the video IDs
for an input of list of movie titles. Adds a column for URLs and video IDs,
and then exports the updated dataset to a csv.
"""

import pandas as pd
import get_youtube_url

def get_youtube_video_ids(data):
    """This function takes in a movie title as a string, then appends 'trailer'
    and searches for this query on YT. Returns the URL.
    """
    #Get movie URL for each movie
    data['youtube_url'] = data['title'].apply(get_youtube_url.get_first_trailer_url)
    #Extract video ID from URL
    data['youtube_id'] = data['youtube_url'].str[32:]
    #Export dataset to csv
    data.to_csv('data/subsetData_withURLS.csv', index=None, header=True)

#Run the lines below to get URLs and video IDs for subsetted data.
df_subset = pd.read_csv('data/imdb_subset_100_10strats')
get_youtube_video_ids(df_subset)
