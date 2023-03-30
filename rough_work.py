# rough_work.py
# Author: Sean Humphreys
# This file is for testing different approaches

import pandas as pd
# from pandas.plotting import table
# import plotly.figure_factory as ff
import seaborn as sns
sns.set_theme(context='notebook', style='darkgrid', palette='pastel', font='sans-serif', font_scale=1, color_codes=True, rc=None)
import matplotlib.pyplot as plt

# download iris data and read it into a dataframe
# url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# df = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# print(df)
df = pd.read_csv('iris.data', sep=',', names=["sepal_length_cm", "sepal_width_cm", "petal_length_cm",
                                              "petal_width_cm", "class"])
# fig = ff.create_table(df)
# fig.update_layout(autosize=True)
# fig.write_image("table_plotly.png", scale=1)

# specify path for export
# path = r'data_summary.txt'

# export DataFrame to text file
# with open(path, 'a') as f:
#    df_string = df.to_string(header=True, index=False)
#    f.write(df_string)

#fig, axes = plt.subplots(2, 2, figsize=(10, 10))

#axes[0, 0].set_title("Sepal Length")
#axes[0, 0].hist(df['sepal_length_cm'], bins=7)

#axes[0, 1].set_title("Sepal Width")
#axes[0, 1].hist(df['sepal_width_cm'], bins=5);

#axes[1, 0].set_title("Petal Length")
#axes[1, 0].hist(df['petal_length_cm'], bins=6);

#axes[1, 1].set_title("Petal Width")
#axes[1, 1].hist(df['petal_width_cm'], bins=6);

plot = sns.FacetGrid(df, hue="class")
plot.map(sns.histplot, "sepal_length_cm", kde=True).add_legend()

plot = sns.FacetGrid(df, hue="class")
plot.map(sns.histplot, "sepal_width_cm", kde=True).add_legend()

plot = sns.FacetGrid(df, hue="class")
plot.map(sns.histplot, "petal_length_cm", kde=True).add_legend()

plot = sns.FacetGrid(df, hue="class")
plot.map(sns.histplot, "petal_width_cm", kde=True).add_legend()

plt.show()
