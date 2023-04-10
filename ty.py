import pandas as pd
import seaborn as sns
#sns.set_theme(context='notebook', style='darkgrid', palette='pastel', font='sans-serif', font_scale=1, color_codes=True, rc=None)
import matplotlib.pyplot as plt
#import numpy as np
import sklearn

# download iris data and read it into a dataframe
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = pd.read_csv(url)

#plt.figure(figsize=(7,4))
#sns.heatmap(iris.corr(),annot=True,cmap='summer')
corr = iris.corr()
#plt.show()