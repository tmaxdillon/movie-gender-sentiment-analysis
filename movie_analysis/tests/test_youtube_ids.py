"""This module runs unit tests over functions in get_youtube_url.ph
and get_youtube_video_ids.py.
"""
import os.path
import unittest
import pandas as pd
import numpy as np
from movie_analysis import get_youtube_url
from movie_analysis import get_youtube_video_ids

class TestYoutubeModules(unittest.TestCase):
    """This class runs unit tests over functions in the modules used to
    extract Youtube video ids.
    """

    def test_single_movie(self):
        """This function tests if the url returned by get_youtube_url
        is correct for the movie "Boy Erased"
        """
        test_movie = "Boy Erased"
        correct_url = "https://www.youtube.com/watch?v=-B71eyB_Onw"
        test_url = get_youtube_url.get_youtube_url(test_movie)
        self.assertEqual(test_url, correct_url)

    def test_single_movie(self):
        """This function tests if the url returned by get_youtube_url
        is a string.
        """
        test_movie = "Boy Erased"
        test_url = get_youtube_url.get_youtube_url(test_movie)
        self.assertTrue(isintance(test_url, str)

    def test_columns(self):
        """ This function tests to make sure  new columns are added.
        """
        df_subset = pd.read_csv('data/imdb_subset_100_10strats')
        df_test = get_youtube_video_ids.get_youtube_video_ids(df_subset)
        self.AssertGreater(len(df_test.columns), len(df_subset.columns))

    def test_column_names(self):
        """ This function tests to make sure the correct columns are added.
        """
        df_subset = pd.read_csv('data/imdb_subset_100_10strats')
        correct_column_names = df_subset.columns.values
        correct_column_names.append("youtube_url")
        correct_column_names.append("youtube_id")
        df_test = get_youtube_video_ids.get_youtube_video_ids(df_subset)
        test_column_names = df_test.columns.values
        self.AssertEqual(correct_column_names, test_columns_names)

    def test_file_output(self):
        """This function tests that a new file is saved"""
        df_subset = pd.read_csv('data/imdb_subset_100_10strats')
        get_youtube_video_ids.get.youtube_video_ids(df_subset)
        self.assertTrue(os.path.isfile('data/subsetData_withURLS.csv'))

if __name__ == '__main__':
    unittest.main()
