
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import json
import matplotlib
import matplotlib.pyplot as plt

#calculate diversity score for a single movie
def compute_diversity_score(cast,wanttoweight):
    castsize = len(cast) #number of cast members
    score = 0 #initialize
    if castsize == 0 or castsize == []: #no cast listed
        score = np.nan #nan for no cast
    else:
        if wanttoweight:
            #asymmetrical sigmoidal curve fit from https://mycurvefit.com/
            weights = [ 0.00557557 + (1.002644 - 0.00557557)/(1 + (x/1.794024)**8.661941)**0.5556762
               for x in np.linspace(1,10,20)] #weight lead roles more (up to 20 roles)
        else:
            weights = np.ones(20)
        if castsize > 20: #more than 20 memebrs in cast
            ind = range(0,20)
        else: #less than 20 members in cast
            ind = range(0,castsize)
        for c in ind: #loop over all cast members
            if cast[c]['gender'] == 1: #female
                score = score + weights[c] #female cast members boost score
                m_all = False #debug boolean
            elif cast[c]['gender'] != 2: #not female nor male gender number
                weights[c] = 0; #discount entry
        if sum(weights[:c+1]) == 0:
            score = np.nan
        else:
            score = score/sum(weights[:c+1]) #take the weighted average of the score
    return score, castsize

#visualize 
def viz_distribution(data,type):
    n_bins = 20 
    if type == 'diversity score':
        fig, ax = plt.subplots()   
        n, bins, patches = plt.hist(data, bins=n_bins, alpha=0.35, edgecolor='k')
        ax.set(xlabel='gender diversity score', ylabel='number of movies',
               title='Histogram of Gender Diversity Score')
    elif type == 'cast size':
        fig, ax = plt.subplots()   
        data = data[np.argwhere(~np.isnan(data))]
        binwidth =10
        n_bins = range(0, int(10*np.floor(max(data)/10)) + binwidth, binwidth)
        n, bins, patches = plt.hist(data, bins=n_bins, alpha=0.35, edgecolor='k', facecolor='g')
        ax.set(xlabel='cast size', ylabel='number of movies',
               title='Histogram of Cast Size')
    ax.grid()
    #median and percentile values
    mean = plt.axvline(data.mean(), color='r', linestyle='dashed', linewidth=1)
    median = plt.axvline(np.percentile(data,50), color='k', linestyle='dashed', linewidth=1)
    ninety = plt.axvline(np.percentile(data,90), color='k', linestyle='dashed', linewidth=1)
    ten = plt.axvline(np.percentile(data,10), color='k', linestyle='dashed', linewidth=1)
    ax.legend((mean, median, ninety, ten), ('mean','median','90%','10%'))
    if type == 'diversity score':
        fig.savefig('Figures/Full_Diversity_Dist.pdf')
    elif type == 'cast size':
        fig.savefig('Figures/Cast_Size_dist.pdf')

