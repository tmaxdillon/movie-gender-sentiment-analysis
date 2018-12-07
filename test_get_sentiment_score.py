import unittest
import get_sentiment_score as gss
import pandas as pd
class TestSentiment(unittest.TestCase):

	def test_oneshot(self):
		df = gss.get_sentiment_score()
	    self.assertFalse(df.empty)

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
