" Unit tests for plotting functions "

# Units tests for plotting functions

import os.path
import numpy as np
from movie_analysis import plot_functions as pf

def test_pdfs_created():
    " Checking for scatter plots and linear regression pdfs saved in Figures "
    file = 'Figures/tmp.pdf'
    pf.scatter_scores([1, 2], [2, 4], file)
    assert os.path.isfile(file) is True
    file2 = 'Figures/tmp2.pdf'
    pf.linear_regression(np.array([1, 2]), np.array([2, 4]), file2)
    assert os.path.isfile(file2) is True


def test_fit():
    " Compare the linear fit against a line "
    test_a = np.array([0, 1, 2, 3, 4, 5])
    test_b = np.array([3, 5, 7, 9, 11, 13])
    fit = pf.linear_regression(test_a, test_b, 'Figures/tmp.pdf')
    assert sum(fit-test_b) == 0
