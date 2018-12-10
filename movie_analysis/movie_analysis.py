# Library imports:
import pandas as pd
#import matplotlib
#import matplotlib.pyplot as plt
import plot_functions as pf
#from .get_sentiment_score import get_sentiment_score, add_row, find_csv_filenames

full_df = pd.read_csv('data/imdb_subset_100_10strats')
GDS = full_df['gender diversity score']
SS = full_df['sentiment_score']

# Plots:
pf.scatter_scores(GDS,SS)
pf.linear_regression(GDS,SS)
