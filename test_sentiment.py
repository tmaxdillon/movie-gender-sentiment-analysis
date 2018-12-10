import os
import unittest
import get_sentiment_score as gss
import analyze_comments_tblob as act
import pandas as pd

class TestSentiment(unittest.TestCase):

	# test get_sentiment_score function
	def test_oneshot(self):
		df = gss.get_sentiment_score()
		self.assertFalse(df.empty)

	def test_edge(self):
		gss.ANALYZED_PATH = "something"
		self.assertRaises(Exception, gss.get_sentiment_score())

	def test_column_names(self):
		self.assertEqual(list(gss.get_sentiment_score()),['movie_id','sentiment_score'])

	# test find_csv_filenames function
	def test_find_csv_oneshot(self):
		self.assertFalse(len(gss.find_csv_filenames(gss.PATH, suffix=".csv")) == 0)

	def test_find_csv_edge(self):
		self.assertRaises(Exception, gss.find_csv_filenames(gss.PATH, ".html"))

	def test_find_csv_2(self):
		if not os.path.isdir("test1"):
			os.mkdir("test1")
		f = open("test1/testing.csv","w+")
		f.close() 
		self.assertTrue(gss.find_csv_filenames("test1", ".csv"),["testing.csv"])

	#test add_row function
	def test_add_row(self):
		test_df = pd.DataFrame(columns=['movie_id','sentiment_score'])
		test_df = gss.add_row(99,1.0,test_df)
		self.assertEqual(test_df.at[0,"movie_id"], 99)
		self.assertEqual(test_df.at[0,"sentiment_score"],1.0)

	#test analyze_comments function
	def test_analyze_pos_comment(self):
		pos_comment = "this is great"
		test2_df = pd.DataFrame([[pos_comment]], columns=["comment"])
		test2_df = act.analyze_comments(test2_df)
		self.assertEqual(test2_df.at[0,"tblob_label"], "1")

	def test_analyze_neg_comment(self):
		pos_comment = "this is awful"
		test2_df = pd.DataFrame([[pos_comment]], columns=["comment"])
		test2_df = act.analyze_comments(test2_df)
		self.assertEqual(test2_df.at[0,"tblob_label"], "0")


suite = unittest.TestLoader().loadTestsFromTestCase(TestSentiment)
_ = unittest.TextTestRunner().run(suite)
