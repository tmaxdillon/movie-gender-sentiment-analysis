" Package for plotting and fitting data "

# Import Packages:
import numpy as np
import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy as sp

# Scatter plot of all movies:
def scatter_scores(gender_diversity_score, sentiment_score, figure_name):
    " Scatter plot of all movies in the subset "
    fig = plt.figure()
    plt.title("Sentiment analysis of YouTube comments on gender diverse films")
    plt.scatter(gender_diversity_score, sentiment_score)
    plt.xlabel('Gender Diversity Score')
    plt.ylabel('Sentiment Analysis Score')
    #plt.show()
    fig.savefig(figure_name)

# Linear Regression:
def linear_regression(gender_diversity_score, sentiment_score, figure_name):
    " Linear regression analysis between scores "
    fig = plt.figure()
    slope, intercept = sp.stats.linregress(gender_diversity_score, sentiment_score)
    plt.title("Sentiment analysis of YouTube comments on gender diverse films")
    plt.scatter(gender_diversity_score, sentiment_score)
    fit = gender_diversity_score*slope+intercept
    plt.plot(gender_diversity_score, fit, 'r--')
    plt.xlabel('Gender Diversity Score')
    plt.ylabel('Sentiment Analysis Score')
    #plt.show()
    fig.savefig(figure_name)
    return fit

# Nonlinear least-squares fit:
def nonlinear_lsf(gender_diversity_score, sentiment_score, figure_name):
    " Nonlinear least-squares fit between scores "
    def func(x_var, a_var, b_var, c_var):
        " nonlinear equation form "
        return a_var*np.exp(-b_var*x_var)+c_var
    popt = curve_fit(func, gender_diversity_score, sentiment_score)
    fig = plt.figure()
    plt.plot(gender_diversity_score, func(gender_diversity_score, *popt), 'r-',
             label='fit:a_var=%5.5f,b_var=%5.3f,c_var=%5.3f' % tuple(popt))
    plt.scatter(gender_diversity_score, sentiment_score, label='all movies')
    plt.xlabel('Gender Diversity Score')
    plt.ylabel('Sentiment Score')
    plt.legend()
    fig.savefig(figure_name)
