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


def table_save(file, output_file):
    # declare a variable for the ff.create table method
    fig = ff.create_table(file)
    #  method to change the look and feel of the table
    fig.update_layout(autosize=False, width=300, height=200)
    # write the table_plotly.png file to the images folder
    fig.write_image(f"script_output/f{output_file}.png", scale=1)
