# Analysis.py
# Author: Sean Humphreys
# Script to read in and analyse the IRIS data set
import os

# # # # # Import Required Libraries # # # # #

# import the pandas module used to read in the data set file as a data frame
import pandas as pd
# Import andrews_curves from pandas.plotting required to produce Andrew's Curves plot
from pandas.plotting import andrews_curves
# Import parallel_coordinates from pandas.plotting required to produce parallel coordinates plot
from pandas.plotting import parallel_coordinates
# Import radviz from pandas.plotting required to produce radviz plot
from pandas.plotting import radviz
# Import lag_plot from pandas.plotting required to produce lag plot
from pandas.plotting import lag_plot
# import plotly module used to create a table of the data for display in the README.md file
import plotly.figure_factory as ff
# import the seaborn module as sns used for plotting data representation - more advanced functionality that matplotlib
import seaborn as sns
# import the matplotlib module used to plot data for visual representation
import matplotlib.pyplot as plt
import csv
import numpy as np
# time library used to save files with current date & time stamp in filename
import time

# # # # # Declare Global Variables # # # # #
# declare a variable to define the Iris Data Set URL

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# # # # # Define Functions # # # # #
# ? need to remove if no functions
# possible functions - function to save tables from dataframe -

# # # # # Read in the data set set from URL # # # # #
print("Reading in the Iris Data Set as a dataframe..........")
# Define data frame as variable iris. Use Pandas to read in file from the URL variable with the column names as defined
# in the list = "names"
# Reference https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv - accessed 30/03/2023

iris = pd.read_csv(url, names=["Sepal Length cms", "Sepal Width cms", "Petal Length cms", "Petal Width cms", "Species"])
#print(iris) # validation check ? remove
print("Data read in complete.")

# # # # # Check source data quality # # # # #
print("Checking for missing data in data set..........")
# The code in this section checks the quality of the source data and writes the output to a table. To achieve this the
# isnull() method is used and transposed to a CSV. Headers are injected into the CSV to make it understandable. The CSV
# is read in as a dataframe and a table based on the dataframe is then saved to file. This is a roundabout way however
# it was the only way to be found to create a table with presentable formatting

# Define a variable to use the check for missing data using the isnull() method
# https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
missing_values_table = iris.isnull().sum().T
# Transpose the table to a csv file
missing_values_table.transpose().to_csv('missing_values.csv', sep=',')

# define headers for the csv file
header = ['Species', 'Missing Values']
# open the csv file in read mode
with open('missing_values.csv', 'r') as fp:
    reader = csv.DictReader(fp, fieldnames=header)

    # use newline='' to avoid adding new CR at end of line
    with open('missing_values_2.csv', 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=reader.fieldnames)
        writer.writeheader()
        header_mapping = next(reader)
        writer.writerows(reader)

# variable to define a data frame for the table
missing_values_table_csv = pd.read_csv('missing_values_2.csv', sep=',')

# declare a variable for the ff.create table method
fig = ff.create_table(missing_values_table_csv)
#  method to change the look and feel of the table
fig.update_layout(autosize=False, width=300, height=200)
# write the table_plotly.png file to the images folder
fig.write_image(f"script_output/missing_data_summary.png", scale=1)

# Delete CSV files no longer needed
os.remove('missing_values.csv')
os.remove('missing_values_2.csv')

print(f"Check complete. Output saved to \"script_output\" folder as missing_data_summary.png")

# # # # # Output Variable to txt file # # # # #

print("Creating a summary of each variable..........")

# Output a summary of each variable to a text file - https://www.statology.org/pandas-to-text-file/ accessed 30/03/2023
# variable that specifies path for outputting of .txt file
path = r'data_summary.txt'
# open path defined above and w to file
with open(path, 'w') as f:
    # define variable to convert the dataframe to a string, include the header and exclude the index
    iris_string = iris.to_string(header=True, index=False)
    # write the iris_string variable to the file path
    f.write(iris_string)

print("Variable summary saved to file called data_summary.txt")
# f = open("data_summary.txt") # validation test
# print(f.read()) # validation test
# print(df)  # validation test
# data.shape # validation test to make sure that there 150 rows of data and number of columns

# # # # # Create a summary table for analysis section # # # # #

# Print statement to let the user know the script is progressing
print('Creating a summary table of the Iris Data Set..........')

# create a summary of the iris data set - min, max, mean, median, SD, etc
summary = iris.describe()
summary_round = iris.describe().T
summary_round.transpose().to_csv('summary_stats.csv', sep=',')
# adding header
header = [' ', 'Sepal Length cm', 'Sepal Width cm', 'Petal Length cm', 'Petal Width cm']
with open('summary_stats.csv', 'r') as fp:
    reader = csv.DictReader(fp, fieldnames=header)

    # use newline='' to avoid adding new CR at end of line
    with open('output.csv', 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=reader.fieldnames)
        writer.writeheader()
        header_mapping = next(reader)
        writer.writerows(reader)

data_summary = pd.read_csv('output.csv', sep=',')

# Write the dataframe to a formatted tables using function
fig3 = ff.create_table(data_summary)
#  method to change the look and feel of the table
fig3.update_layout(autosize=False, width=700, height=200)
# write the table_plotly.png file to the images folder
fig3.write_image(f"script_output/data_summary.png", scale=1)

# Clean up unnecessary files
os.remove("output.csv")

# Clean up unnecessary files
os.remove("summary_stats.csv")

print(f"Data summary table complete. Output saved to \"script_output\" folder as data_summary.png")

# # # # # Create summary table of data for appendix 1 # # # # #

print('Creating a summary table of full data set..........')

# following code snippet from https://www.delftstack.com/howto/python-pandas/pandas-png/ - accessed 30/03/2023
# variable called fig to define function to create a table using plotly module for the dataframe "df"
fig4 = ff.create_table(iris)
#  method to change the look and feel of the table
fig4.update_layout(autosize=True)
# write the table_plotly.png file to the images folder
fig4.write_image(f"script_output/full_data_set_table.png", scale=1)

print(f"Full data set summary table complete. Output saved to \"script_output\" folder as full_data_set_table.png")

# # # # # Create & save histograms # # # # #

print('Creating histograms analysis of the data set..........')

# define theme for sns - https://seaborn.pydata.org/generated/seaborn.set_theme.html - accessed 30/03/2023
# sns.set_theme(context='notebook', style='darkgrid', palette='pastel', font='sans-serif', font_scale=1,
#              color_codes=True, rc=None)
# code to create histograms using seaborn module - https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
# - accessed 30/03/2023
plot = sns.FacetGrid(iris, hue="Species", height=5)
# originally used distplot function but got message that it is being depreciated, when code was run, so used
# histplot function instead - https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751 - accessed 30/03/2023
plot.map(sns.histplot, "Sepal Length cms", kde=True).add_legend().set(title='Sepal Length Distribution')
# save output to images folder - https://www.marsja.se/how-to-save-a-seaborn-plot-as-a-file-e-g-png-pdf-eps-tiff/
# - accessed 30/03/2023
plt.savefig('script_output/sepal_length_histogram.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Sepal Width cms", kde=True).add_legend().set(title='Sepal Width Distribution')
plt.savefig('script_output/sepal_width_histogram.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Petal Length cms", kde=True).add_legend().set(title='Petal Length Distribution')
plt.savefig('script_output/petal_length_histogram.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Petal Width cms", kde=True).add_legend().set(title='Petal Width Distribution')
plt.savefig('script_output/petal_width_histogram.png', bbox_inches='tight')

plt.show()

print('Histograms have been saved in the \"script_output\" folder')

# # # # # Create & save box plots # # # # #
# Reference - https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/


# function to pass arguments to sns.boxplot method

def graph(y):
    sns.boxplot(x="Species", y=y, data=iris)


# plot size
plt.figure(figsize=(10, 10))
# Adding the subplot at the specified
# grid position
plt.subplot(221)
graph('Sepal Length cms')

plt.subplot(222)
graph('Sepal Width cms')

plt.subplot(223)
graph('Petal Length cms')

plt.subplot(224)
graph('Petal Width cms')


# Save plot to file
plt.savefig('images/plots/box_plots/box_plots.png')
plt.show()

# # # # # Outliers Demo # # # # #

# create a deep copy of the original Iris dataframe - https://www.w3schools.com/python/pandas/ref_df_copy.asp
outlier_test = iris.copy()

# remove all rows so that only Iris-setosa remains
# https://www.shanelynn.ie/pandas-drop-delete-dataframe-rows-columns/ - accessed 10/04/2023
outlier_test.drop(index=outlier_test.index[50:150], axis=0, inplace=True)

# plot the boxplot demonstrating outliers
sns.boxplot(x='Species', y="Petal Length cms", data=outlier_test).set_title("Petal Length Outliers")
plt.savefig('images/plots/box_plots/outliers_box_plots.png')
plt.show()

# the following lines of code are based on - https://www.geeksforgeeks.org/detect-and-remove-the-outliers-using-python/
# accessed- 10/04/2023
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

# # # # # Violin PLots # # # # #
def violin_graph(y):
    sns.violinplot(x="Species", y=y, data=iris)


# plot size
plt.figure(figsize=(10, 10))
# Adding the subplot at the specified
# grid position
plt.subplot(221)
violin_graph('Sepal Length cms')

plt.subplot(222)
violin_graph('Sepal Width cms')

plt.subplot(223)
violin_graph('Petal Length cms')

plt.subplot(224)
violin_graph('Petal Width cms')

plt.savefig('images/plots/violin_plots/violin_plots.png')
plt.show()

# # # # # Generate Heatmap # # # # #

# Read in the data set
# create a deep copy of the original Iris dataframe - https://www.w3schools.com/python/pandas/ref_df_copy.asp
iris_heatmap = iris.copy()
# Drop the species column - solved issue using this post
# https://stackoverflow.com/questions/69660844/count-not-conver-string-to-float-using-iris-dataset - accessed 10/04/2023
iris_heatmap.drop('Species', axis=1, inplace=True)
# Pandas dataframe.corr() method used to find the pairwise correlation of all columns in the dataframe
# https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ - accessed 10/04/2023
corr = iris_heatmap.corr()
# The following lines of code to format the heatmap were taken from here
# https://www.analyticsvidhya.com/blog/2021/06/guide-to-data-visualization-with-python-part-1/ - accessed 10/04/2023
# and here https://stackoverflow.com/questions/32723798/how-do-i-add-a-title-and-axis-labels-to-seaborn-heatmap -
# accessed 13/04/2023
fig, ax = plt.subplots()
img = ax.imshow(corr.values,cmap = "magma_r")
# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)
ax.set_title('Iris Data Set Heatmap')
cbar = ax.figure.colorbar(img, ax=ax ,cmap='')
plt.setp(ax.get_xticklabels(), rotation=30, ha="right",
         rotation_mode="anchor")
# text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        if corr.iloc[i, j]<0:
            text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")
        else:
            text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="white")

plt.savefig('images/plots/heatmap/heatmap.png', bbox_inches='tight')
plt.show()

# # # # # Create Pairplot # # # # #
# Pairplots based on code at - http://uconn.science/wp-content/uploads/2017/07/iris_visualization.html
# Create the pairplot with Kernel Density Estimation as opposed histograms in the diagonal elements
sns.pairplot(iris, hue="Species", height=3, diag_kind="kde")
plt.savefig('images/plots/pairplots/pairplot.png')
plt.show()

# # # # # Andrews Curves # # # # #
# code from - http://uconn.science/wp-content/uploads/2017/07/iris_visualization.html#Andrews-Curves
andrews_curves(iris, "Species")
plt.savefig('images/plots/multivariate/andrews_curves.png')
plt.show()

# # # # # Parallel Coordinates # # # # #
# code from - http://uconn.science/wp-content/uploads/2017/07/iris_visualization.html#parallel_coordinates
parallel_coordinates(iris, "Species")
plt.savefig('images/plots/multivariate/parallel_coordinates.png')
plt.show()

# # # # # RadViz # # # # #
# code frm - http://uconn.science/wp-content/uploads/2017/07/iris_visualization.html#radviz
radviz(iris, "Species")
plt.savefig('images/plots/multivariate/radviz.png')
plt.show()

# # # # # Lag Plot # # # # #
# code from - https://towardsdatascience.com/6-lesser-known-pandas-plotting-tools-fda5adb232ef
iris.drop('Species', axis=1, inplace=True)
plt.figure(figsize=(10,6))
lag_plot(iris)
plt.savefig('images/plots/multivariate/lag_plot.png')
plt.show()