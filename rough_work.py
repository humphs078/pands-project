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
df = pd.read_csv(url, names=["Sepal Length cm", "Sepal Width cm", "Petal Length cm", "Petal Width cm", "Species"])
# print(df)
# df = pd.read_csv('iris.data', sep=',', names=["Sepal Length cm", "Sepal Width cm", "Petal Length cm",
# "Petal Width cm", "Species"])

# data = df.drop_duplicates(subset ="Species",)

# print(df.value_counts("Species"))


#sns.countplot(x='Species', data=df, )
# plt.show()

def graph(y):
    sns.boxplot(x="Species", y=y, data=df)


plt.figure(figsize=(10, 10))

# Adding the subplot at the specified
# grid position
plt.subplot(221)
graph('Sepal Length cm')

plt.subplot(222)
graph('Sepal Width cm')

plt.subplot(223)
graph('Petal Length cm')

plt.subplot(224)
graph('Petal Width cm')

plt.show()
