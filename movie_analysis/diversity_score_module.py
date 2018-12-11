"""Package of functions for diversity score"""
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
<<<<<<< HEAD
=======
import json
import matplotlib
matplotlib.use('PS')
>>>>>>> 9817f4484dcf0eb073ed2d28f1921eaef943d62c
import matplotlib.pyplot as plt

#calculate diversity score for a single movie
def compute_diversity_score(cast, wanttoweight):
    """ This function computes diversity score for a single movie"""
    castsize = len(cast) #number of cast members
    score = 0 #initialize
    if castsize == 0 or castsize == []: #no cast listed
        score = np.nan #nan for no cast
    else:
        if wanttoweight:
            #asymmetrical sigmoidal curve fit from https://mycurvefit.com/
            weights = [0.00557557 + (1.002644 - 0.00557557)/(1 + (x/1.794024)**8.661941)**0.5556762
                       for x in np.linspace(1, 10, 20)] #weight lead roles more (up to 20 roles)
        else:
            weights = np.ones(20)
        if castsize > 20: #more than 20 memebrs in cast
            ind = range(0, 20)
        else: #less than 20 members in cast
            ind = range(0, castsize)
        for cha in ind: #loop over all cast members
            if cast[cha]['gender'] == 1: #female
                score = score + weights[cha] #female cast members boost score
            elif cast[cha]['gender'] != 2: #not female nor male gender number
                weights[cha] = 0 #discount entry
        if sum(weights[:cha+1]) == 0:
            score = np.nan
        else:
            score = score/sum(weights[:cha+1]) #take the weighted average of the score
    return score, castsize

#visualize
def viz_distribution(data, type):
    """This function visualizes distribution for cast size and diversity score"""
    n_bins = 20
    if type == 'diversity score':
        fig, axe = plt.subplots()
        plt.hist(data, bins=n_bins, alpha=0.35, edgecolor='k')
        axe.set(xlabel='gender diversity score', ylabel='number of movies',
                title='Histogram of Gender Diversity Score')
    elif type == 'cast size':
        fig, axe = plt.subplots()
        data = data[np.argwhere(~np.isnan(data))]
        binwidth = 10
        n_bins = range(0, int(10*np.floor(max(data)/10)) + binwidth, binwidth)
        plt.hist(data, bins=n_bins, alpha=0.35, edgecolor='k', facecolor='g')
        axe.set(xlabel='cast size', ylabel='number of movies',
                title='Histogram of Cast Size')
    axe.grid()
    #median and percentile values
    mean = plt.axvline(data.mean(), color='r', linestyle='dashed', linewidth=1)
    median = plt.axvline(np.percentile(data, 50), color='k', linestyle='dashed', linewidth=1)
    ninety = plt.axvline(np.percentile(data, 90), color='k', linestyle='dashed', linewidth=1)
    ten = plt.axvline(np.percentile(data, 10), color='k', linestyle='dashed', linewidth=1)
    axe.legend((mean, median, ninety, ten), ('mean', 'median', '90%', '10%'))
    if type == 'diversity score':
        fig.savefig('Figures/Full_Diversity_Dist.pdf')
    elif type == 'cast size':
        fig.savefig('Figures/Cast_Size_dist.pdf')

#extract subset of data
def get_subset(dframe, strata, subsetno):
    """This function extracts a subset of the data"""
    df_subset = pd.DataFrame(columns=list(dframe)) #initialize
    df_real = dframe.dropna() #get rid of nans
    edges = np.linspace(0, 1, strata+1) #edges of data strata
    for i in range(0, strata):
        df_temp = df_real[(df_real['gender diversity score'] > edges[i]) &
                          (df_real['gender diversity score'] < edges[i+1])]
        temp_ind = np.round(np.linspace(0, len(df_temp)-1, subsetno/strata))
        df_subset = pd.concat([df_subset,
                               df_temp.sort_values(by=['gender diversity score']).
                               iloc[temp_ind, :].reset_index(drop=True)], ignore_index=True)
    return df_subset
