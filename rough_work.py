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

summary = df.describe()
summary_round = df.describe().T
print(summary_round.head())

summary_round.transpose().to_csv('summary stats.csv', sep=',')

# adding header
header = [' ', 'Sepal Length cm', 'Sepal Width cm', 'Petal Length cm', 'Petal Width cm']

with open('summary stats.csv', 'r') as fp:
    reader = csv.DictReader(fp, fieldnames=header)

    # use newline='' to avoid adding new CR at end of line
    with open('output.csv', 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=reader.fieldnames)
        writer.writeheader()
        header_mapping = next(reader)
        writer.writerows(reader)


data_summary = pd.read_csv('output.csv', sep=',')

fig2 = ff.create_table(data_summary)
#  method to change the look and feel of the table
fig2.update_layout(autosize=False, width=700, height=200)
# write the table_plotly.png file to the images folder
fig2.write_image("images/tables/data_summary.png", scale=1)
