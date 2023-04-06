# rough_work.py
# Author: Sean Humphreys
# This file is for testing different approaches

import pandas as pd
import csv
from pandas.plotting import table
import plotly.figure_factory as ff
import plotly.express as px
import seaborn as sns
sns.set_theme(context='notebook', style='darkgrid', palette='pastel', font='sans-serif', font_scale=1, color_codes=True, rc=None)
import matplotlib.pyplot as plt
import numpy as np
import sklearn

# download iris data and read it into a dataframe
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, names=["Sepal Length cms", "Sepal Width cms", "Petal Length cms", "Petal Width cms", "Species"])


def graph(y):
    sns.boxplot(x="Species", y=y, data=iris)


# plot size
plt.figure(figsize=(10, 10))
# Adding the subplot at the specified
# grid position
plt.subplot(221)
graph('Sepal Length cms')

plt.subplot(222)
graph('Sepal Width cms')

plt.subplot(223)
graph('Petal Length cms')

plt.subplot(224)
graph('Petal Width cms')


# Save plot to file
plt.savefig('images/plots/box_plots/box_plots.png')
plt.show()

# # # # # Outliers Demo # # # # #
sns.boxplot(x='Sepal Width cms', data=iris).set_title("Sepal Width Outliers")


# Define Q1 variable for numpy percentile method for the dataset column sepal width
Q1 = np.percentile(iris['Sepal Width cms'], 25,
                   method='midpoint')
# Define Q1 variable for numpy percentile method for the dataset column sepal width
Q3 = np.percentile(iris['Sepal Width cms'], 75,
                   method='midpoint')
IQR = Q3 - Q1

# Upper bound
upper = np.where(iris['Sepal Width cms'] >= (Q3 + 1.5 * IQR))

# Lower bound
lower = np.where(iris['Sepal Width cms'] <= (Q1 - 1.5 * IQR))

# Removing the Outliers
iris.drop(upper[0], inplace=True)
iris.drop(lower[0], inplace=True)

# print("New Shape: ", iris.shape) # validation test

# plot box plot with outliers removed and save file
sns.boxplot(x='Sepal Width cms', data=iris).set_title("Sepal Width Outliers Removed")
plt.show()