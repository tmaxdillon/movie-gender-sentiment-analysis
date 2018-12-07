import unittest
import get_sentiment_score as gss
import pandas as pd
class TestSentiment(unittest.TestCase):

	def test_oneshot(self):
		df = gss.get_sentiment_score()
		self.assertFalse(df.empty)

	def test_edge(self):
		ANALYZED_PATH = "something"
		self.assertRaises(Exception, gss.get_sentiment_score())

suite = unittest.TestLoader().loadTestsFromTestCase(TestSentiment)
_ = unittest.TextTestRunner().run(suite)
