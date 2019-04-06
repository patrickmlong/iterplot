"""
This module generates iterative plots to expedite EDA
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class IterativePlot:

	def __init__(self, df, outcome_col):
		self.outcome_col = outcome_col
		self.df_pos = df[df[outcome_col] == 1]
        	self.df_neg = df[df[outcome_col] == 0]

		
	def iterative_distplot(self, col_list = []):
	
		"""
		args:
			col_list: list of columns for plotting
		"""

		# Instantiate a figure object for OOP figure manipulation.
		fig = plt.figure()

		# Create 'for loop' to enumerate up to 10 columns
		for index, col in enumerate(col_list[0:10):

		    # Enumerate starts at index 0, need to add 1 for subplotting
		    index +=1

		    # Create axes object for position i
		    ax = fig.add_subplot(3,4,index)

		    # Plot via histogram
		    sns.distplot(self.df_pos[col], kde=True, label='positive')
		    sns.distplot(self.df_neg[col], kde=True, label='negative')

		    ax.set_title(col)

		sns.set_style("whitegrid")
		plt.tight_layout()
		plt.legend()
		plt.show()


	def iterative_boxplot(self, col_list = []):
	
		"""
		args:
			col_list: list of columns for plotting
		"""

		# Instantiate a figure object for OOP figure manipulation.
		fig = plt.figure()

		# Create 'for loop' to enumerate up to 10 columns
		for index, col in enumerate(col_list[0:10]):

		    # Enumerate starts at index 0, need to add 1 for subplotting
		    index +=1

		     # Create axes object for position i
		     ax = fig.add_subplot(3,4,index)

		     # Plot via histogram .
		     ax.boxplot([self.df_pos[col], self.def_neg[col]])

		     ax.set_title(col)

		sns.set_style("whitegrid")
		plt.tight_layout()
		plt.legend()
		plt.show()
