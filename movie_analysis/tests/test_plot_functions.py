# Units tests for plotting functions

from movie_analysis import plot_functions as pf
import os.path

def test_pdfs_created():
	# Check that there are scatter plots and linear regressions saved to Figures
	file = '../Figures/tmp.pdf'
	pf.scatter_scores([1,2],[2,4],file)
	assert os.path.isfile(file) is True
	
	file2 = '..Figures/tmp2.pdf'
	pf.linear_regression([1,2],[2,4],file2)
	assert os.path.isfile(file2) is True


def test_fit():
	# Compare the linear fit against a line
	a = [0, 1, 2, 3, 4, 5]
	b = [3, 6, 7, 9, 11, 13]
	out = pf.linear_regression(a,b,'..Figures/tmp.pdf')
	assert fit == b is True

