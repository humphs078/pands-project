# rough_work.py
# Author: Sean Humphreys
# This file is for testing different approaches

import pandas as pd
import seaborn as sns
#sns.set_theme(context='notebook', style='darkgrid', palette='pastel', font='sans-serif', font_scale=1, color_codes=True, rc=None)
import matplotlib.pyplot as plt
import numpy as np
import sklearn

# download iris data and read it into a dataframe
url = 'https://datahub.io/machine-learning/iris/r/iris.csv'
iris = pd.read_csv(url)

print(iris.info())
print(iris.head())

plot = sns.FacetGrid(iris, hue="class")
plot.map(plt.hist, "sepallength")

plot = sns.FacetGrid(iris, hue="class")
plot.map(plt.hist, "sepalwidth")

plot = sns.FacetGrid(iris, hue="class")
plot.map(plt.hist, "petallength")

plot = sns.FacetGrid(iris, hue="class")
plot.map(plt.hist, "petalwidth")

plt.show()