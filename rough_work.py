# rough_work.py
# Author: Sean Humphreys
# This file is for testing different approaches

import pandas as pd
import seaborn as sns
#sns.set_theme(context='notebook', palette='pastel', font='sans-serif', font_scale=1, color_codes=True, rc=None)
import matplotlib.pyplot as plt
import numpy as np
import sklearn

# download iris data and read it into a dataframe
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = pd.read_csv(url, names=["Sepal Length cms", "Sepal Width cms", "Petal Length cms",
                                     "Petal Width cms", "Species"])

from pandas.plotting import andrews_curves
andrews_curves(iris, "Species")
plt.show()

from pandas.plotting import parallel_coordinates
parallel_coordinates(iris, "Species")
plt.show()

from pandas.plotting import radviz
radviz(iris, "Species")
plt.show()


from pandas.plotting import lag_plot
iris.drop('Species', axis=1, inplace=True)
plt.figure(figsize=(10,6))
lag_plot(iris)
plt.show()

