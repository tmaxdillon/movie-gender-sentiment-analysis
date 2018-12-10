import pandas as pd
import numpy as np
import get_YT_URL

#The following script uses the get_YT_URL function to get the URLs for the
#movie trailers and their video IDs

#Load the subsetted movie data set
df_subset = pd.read_csv('imdb_subset_100_10strats')
#Get movie URL for each movie
df_subset['YouTubeTrailerURL'] = df_subset['title'].apply(get_YT_URL)
#Extract video ID from URL
df_subset['videoIDs'] = df_subset['YouTubeTrailerURL'].str[32:]
#Export dataset to csv
export_csv = df_subset.to_csv (r'/Users/eric/MovieProject/subsetData_withURLS.
csv', index = None, header=True)
