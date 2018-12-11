
# coding: utf-8

# In[ ]:


"""This module runs unit tests over functions in diversity_score_module"""

import os.path
import unittest
import json
import pandas as pd
import numpy as np
from movie_analysis import diversity_score_module as dsm

class TestDivScore(unittest.TestCase):


    """This class runs unit tests over functions in the diversity_score_module"""


    # test compute_diversity_score function
    def test_correcttype(self):
        """This function tests if the values returned by compute_diversity_score
        are the correct type
        """
        cast = json.loads(pd.read_csv('../data/raw_data/tmdb_5000_credits.csv')
                          ['cast'][5]) #load dataset
        [dvs, cas] = dsm.compute_diversity_score(cast, True)
        self.assertTrue(isinstance(dvs) == np.float64 & isinstance(cas) == np.float64)

    def test_savefig(self):
        """This function tests that a figure is saved when viz_distribution is run"""
        dsm.viz_distribution(np.array([2, 3, 1, 8, 3, 8]), 'diversity score')
        self.assertTrue(os.path.isfile('Figures/Full_Diversity_Dist.pdf'))

    def test_subsetrows(self):
        """This function tests if the returned dataframe has the correct number of rows
        """
        dframe = pd.read_csv('../data/raw_data/tmdb_5000_credits.csv')
        subsetno = 70
        strata = 10
        subset = dsm.get_subset(dframe, strata, subsetno)
        self.assertEqual(len(subset), subsetno)
