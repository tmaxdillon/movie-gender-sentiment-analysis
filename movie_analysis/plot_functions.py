# Import Packages:
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as stats

# Scatter plot of all movies:
def scatter_scores(GDS,SS):
	fig = plt.figure()
	plt.title("Sentiment analysis of YouTube comments on gender diverse films")
	plt.scatter(GDS,SS)
	plt.xlabel('Gender Diversity Score')
	plt.ylabel('Sentiment Analysis Score')
	#plt.show()
	fig.savefig('scatter.pdf')

# Linear Regression:
def linear_regression(GDS,SS):
	fig = plt.figure()
	slope, intercept, r_value, p_value, std_err = stats.linregress(GDS,SS)
	plt.title("Sentiment analysis of YouTube comments on gender diverse films")
	plt.scatter(GDS,SS)
	plt.plot(GDS,GDS*slope+intercept,'r--')
	plt.xlabel('Gender Diversity Score')
	plt.ylabel('Sentiment Analysis Score')
	#plt.show()
	fig.savefig('linear_fit.pdf')

# Nonlinear least-squares fit:
def nonlinear_LSF(GDS,SS):
	def func(x,a,b,c):
		return a*np.exp(-b*x)+c
	popt, pcov = curve_fit(func,GDS,SS)
	fig = plt.figure()
	plt.plot(CGD,func(GDS,*popt),'r-',label='fit:a=%5.5f,b=%5.3f,c=%5.3f' % tuple(popt))
	plt.scatter(GDS,SS,label='all movies')
	plt.xlabel('GDS')
	plt.ylabel('Sentiment Score')
	plt.legend()
	#plt.show()
	fig.savefig('nonlinear_LSF.pdf')
