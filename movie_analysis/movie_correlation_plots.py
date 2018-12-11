" Import data and produce pdf plots, including curve fitting "

# Library imports:
import pandas as pd
import plot_functions as pf

FULL_DF = pd.read_csv('data/imdb_subset_100_10strats')
GDS = FULL_DF['gender diversity score']
SS = FULL_DF['sentiment_score']

# Plots:
pf.scatter_scores(GDS, SS, 'Figures/scatter.pdf')
pf.linear_regression(GDS, SS, 'Figures/linear_fit.pdf')
