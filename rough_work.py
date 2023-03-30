# rough_work.py
# Author: Sean Humphreys
# This file is for testing different approaches

import pandas as pd
# import matplotlib.pyplot as plt
# from pandas.plotting import table
# import plotly.figure_factory as ff

# download iris data and read it into a dataframe
# url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# df = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# print(df)
df = pd.read_csv('iris.data', sep=',', names=["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm", "class"])
# fig = ff.create_table(df)
# fig.update_layout(autosize=True)
# fig.write_image("table_plotly.png", scale=1)
