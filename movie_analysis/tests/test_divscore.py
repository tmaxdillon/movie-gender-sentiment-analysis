
# coding: utf-8

# In[ ]:


"""This module runs unit tests over functions in diversity_score_module"""

import os.path
import unittest
import pandas as pd
from movie_analysis import diversity_score_module as dsm

class TestDivScore(unittest.TestCase):


    """This class runs unit tests over functions in the diversity_score_module"""


    # test compute_diversity_score function
    def test_correcttype(self):
        """This function tests if the values returned by compute_diversity_score 
        are the correct type
        """

        [ds,cs] = dsm.compute_diversity_score()
        self.assertTrue(type.ds == np.float64 & type.cs == np.float64)

    def test_savefig(self):
        """This function tests that a figure is saved when viz_distribution is run"""
        file = 'Figures/Full_Diversity_Dist.pdf'
        dsm.viz_distribution([1,2,3,4,5,6,7],'diversity score')
        assert os.path.isfile(file) is True

    def test_subsetrows(self):
        """This function tests if the returned dataframe has the correct number of rows
        """
        
        subsetno = 70
        strata = 10
        subset = dsm.get_subset(df,strata,subsetno)
        self.assertEqual(len(subset),subsetno)



