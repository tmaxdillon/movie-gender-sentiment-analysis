# Units tests for plotting functions

from movie_analysis import plot_functions as pf
import os.path
import numpy as np

def test_pdfs_created():
	# Check that there are scatter plots and linear regressions saved to Figures
	file = 'Figures/tmp.pdf'
	pf.scatter_scores([1,2],[2,4],file)
	assert os.path.isfile(file) is True
	
	file2 = 'Figures/tmp2.pdf'
	fit = pf.linear_regression(np.array([1,2]),np.array([2,4]),file2)
	assert os.path.isfile(file2) is True


def test_fit():
	# Compare the linear fit against a line
	a = np.array([0, 1, 2, 3, 4, 5])
	b = np.array([3, 6, 7, 9, 11, 13])
	fit = pf.linear_regression(a,b,'Figures/tmp.pdf')
	assert np.all(fit == b) is True
