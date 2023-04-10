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
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

outlier_test = pd.read_csv(url, names=["Sepal Length cms", "Sepal Width cms", "Petal Length cms",
                                     "Petal Width cms", "Species"])

outlier_test.drop(index=outlier_test.index[50:150], axis=0, inplace = True)

sns.boxplot(x='Species', y="Petal Length cms", data=outlier_test).set_title("Petal Length Outliers")
plt.savefig('images/plots/box_plots/outliers_box_plots.png')
plt.show()

# Define Q1 variable for numpy percentile method for the dataset column sepal width
Q1 = np.percentile(outlier_test['Petal Length cms'], 25,
                   method='midpoint')
# Define Q1 variable for numpy percentile method for the dataset column sepal width
Q3 = np.percentile(outlier_test['Petal Length cms'], 75,
                   method='midpoint')
IQR = Q3 - Q1

# Upper bound
upper = np.where(outlier_test['Petal Length cms'] >= (Q3 + 1.5 * IQR))

# Lower bound
lower = np.where(outlier_test['Petal Length cms'] <= (Q1 - 1.5 * IQR))

# Removing the Outliers
outlier_test.drop(upper[0], inplace=True)
outlier_test.drop(lower[0], inplace=True)

# plot box plot with outliers removed and save file
sns.boxplot(x='Species', y="Petal Length cms", data=outlier_test).set_title("Petal Length Outliers Removed")
plt.savefig('images/plots/box_plots/no_outliers_box_plots.png')
plt.show()
