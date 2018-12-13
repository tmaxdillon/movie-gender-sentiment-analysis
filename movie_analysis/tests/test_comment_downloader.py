"""This module runs unit tests over functions in the comment_downloader.py"""

import unittest
import comment_downloader as cdr

class TestDownloader(unittest.TestCase):

    """This class runs unit tests over functions in the comment_downloader
    """

    # test get_sentiment_score function
    def test_oneshot(self):
        """This function tests if the downloader print the desired error
        message when no input is given
        """
        self.assertRaises(Exception, cdr.main())
    
    def test_edge(self):
        """This function tests that an exception is raised
        if the wrong path name is provided
        """

        ANALYZED_PATH = "something"
        self.assertRaises(Exception, cdr.main(ANALYZED_PATH))

    def test_download_from_list_oneshot(self):
        """This function tests if the function raises desired error
        message when no input is given
        """
        
        self.assertRaises(Exception, cdr.download_from_list())
        
    def test_download_from_list_edge(self):
        """This function tests that an exception is raised
        if the wrong path name is provided
        """

        ANALYZED_PATH = "something"
        self.assertRaises(Exception, cdr.download_from_list(ANALYZED_PATH))
    
    def test_write_csv_oneshot(self):
        """This function tests if the function raises desired error
        message when no input is given
        """
        
        self.assertRaises(Exception, cdr.write_csv())
        
    def test_write_csv_edge(self):
        """This function tests that an exception is raised
        if the wrong ids are provided
        """

        ANALYZED_Y_ID = "something"
        ANALYZED_M_ID = "somethingsomething"
        self.assertRaises(Exception, cdr.write_csv(ANALYZED_Y_ID, ANALYZED_M_ID))
    
    def test_download_comments_oneshot(self):
        """This function tests if the function raises desired error
        message when no input is given
        """
        
        self.assertRaises(Exception, cdr.download_comments())
        
    def test_download_comments_edge(self):
        """This function tests that an exception is raised
        if the wrong id is provided
        """

        ANALYZED_ID = "something"
        self.assertRaises(Exception, cdr.download_comments(ANALYZED_ID))

    def test_ajax_request_oneshot(self):
        """This function tests if the function raises desired error
        message when no input is given
        """
        
        self.assertRaises(Exception, cdr.ajax_request())
        
    def test_ajax_request_edge(self):
        """This function tests that an exception is raised
        if the wrong data is provided
        """

        ANALYZED_DATA = "something"
        self.assertRaises(Exception, cdr.ajax_request(ANALYZED_DATA))
    
    def test_extract_reply_cids_oneshot(self):
        """This function tests if the function raises desired error
        message when no input is given
        """
        
        self.assertRaises(Exception, cdr.extract_reply_cids())
        
    def test_extract_reply_cids_edge(self):
        """This function tests that an exception is raised
        if the wrong input is provided
        """

        ANALYZED_INPUT = "not an html"
        self.assertRaises(Exception, cdr.extract_reply_cids(ANALYZED_INPUT))
    
    def test_extract_comments_oneshot(self):
        """This function tests if the function raises desired error
        message when no input is given
        """
        
        self.assertRaises(Exception, cdr.extract_comments())
        
    def test_extract_comments_edge(self):
        """This function tests that an exception is raised
        if the wrong input is provided
        """

        ANALYZED_INPUT = "not an html"
        self.assertRaises(Exception, cdr.extract_comments(ANALYZED_INPUT))

    def test_find_value_oneshot(self):
        """This function tests if the function raises desired error
        message when no input is given
        """
        
        self.assertRaises(Exception, cdr.find_value())
        
    def test_find_value_edge(self):
        """This function tests that an exception is raised
        if the wrong input is provided
        """
        
        ANALYZED_INPUT = "not an html"
        ANALYZED_KEY = "not a key"
        self.assertRaises(Exception, cdr.find_value(ANALYZED_INPUT, ANALYZED_KEY))


SUITE = unittest.TestLoader().loadTestsFromTestCase(TestDownloader)
_ = unittest.TextTestRunner().run(SUITE)