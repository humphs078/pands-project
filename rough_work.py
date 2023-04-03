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

# download iris data and read it into a dataframe
# url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# df = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# print(df)
df = pd.read_csv('iris.data', sep=',', names=["Sepal Length cm", "Sepal Width cm", "Petal Length cm",
                                              "Petal Width cm", "Species"])

data = df.drop_duplicates(subset ="Species",)

print(df.value_counts("Species"))


sns.countplot(x='Species', data=df, )
plt.show()

#fig2 = ff.create_table(data)
#  method to change the look and feel of the table
#fig2.update_layout(autosize=False, width=700, height=200)
# write the table_plotly.png file to the images folder
#fig2.write_image("images/tables/data_summary2.png", scale=1)
