# Analysis.py
# Author: Sean Humphreys
# Script to read in and analyse the IRIS data set


# # # # # Import Required Libraries # # # # #

# import the pandas module used to read in the data set file as a data frame
import pandas as pd
# import plotly module used to create a table of the data for display in the README.md file
import plotly.figure_factory as ff
# import the seaborn module as sns used for plotting data representation - more advanced functionality that matplotlib
import seaborn as sns
# import the matplotlib module used to plot data for visual representation
import matplotlib.pyplot as plt
import csv
import numpy as np

# # # # # Declare Global Variables # # # # #
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data' # declare a variable to define the
# Iris Data Set URL

# # # # # Set Themes # # # # #

# Set Seaborn theme to use pastel colours
#sns.set_theme(context='notebook', style='darkgrid', palette='pastel', font='sans-serif', font_scale=1, color_codes=True,
#              rc=None)

# # # # # Read in the data set set from URL # # # # #

# Define data frame as variable iris. Use Pandas to read in file from the URL variable with the column names as defined
# in the list variable called "names"
# Reference https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv - accessed 30/03/2023

iris = pd.read_csv(url, names=["Sepal Length cms", "Sepal Width cms", "Petal Length cms", "Petal Width cms", "Species"])
# print(iris) # validation check ? remove

# # # # # Check source data quality # # # # #

# The code in this section checks the quality of the source data and writes the output to a table

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
fig.write_image("images/tables/missing_values.png", scale=1)

# # # # # Output to txt file # # # # #

# Output a summary of each variable to a text file - https://www.statology.org/pandas-to-text-file/ accessed 30/03/2023
# variable that species path for outputting of .txt file
path = r'data_summary.txt'
# open path defined above and w to file
with open(path, 'w') as f:
    # define variable to convert the dataframe to a string, include the header and exclude the index
    iris_string = iris.to_string(header=True, index=False)
    # write the iris_string variable to the file path
    f.write(iris_string)

# ? need to remove next statements for final submission
# f = open("data_summary.txt") # validation test
# print(f.read()) # validation test
# print(df)  # validation test
# data.shape # validation test to make sure that there 150 rows of data and number of columns

# # # # # Create a summary table for analysis section # # # # #

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

fig3 = ff.create_table(data_summary)
#  method to change the look and feel of the table
fig3.update_layout(autosize=False, width=700, height=200)
# write the table_plotly.png file to the images folder
fig3.write_image("images/tables/data_summary.png", scale=1)

# # # # # Create summary table of data for appendix 1 # # # # #

# following code snippet from https://www.delftstack.com/howto/python-pandas/pandas-png/ - accessed 30/03/2023
# variable called fig to define function to create a table using plotly module for the dataframe "df"
fig4 = ff.create_table(iris)
#  method to change the look and feel of the table
fig4.update_layout(autosize=True)
# write the table_plotly.png file to the images folder
fig4.write_image("images/tables/iris_data_set_full.png", scale=1)

# # # # # Create & save histograms # # # # #

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
plt.savefig('images/plots/histograms/sepal_length_histogram.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Sepal Width cms", kde=True).add_legend().set(title='Sepal Width Distribution')
plt.savefig('images/plots/histograms/sepal_width_histogram.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Petal Length cms", kde=True).add_legend().set(title='Petal Length Distribution')
plt.savefig('images/plots/histograms/petal_length_histogram.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Petal Width cms", kde=True).add_legend().set(title='Petal Width Distribution')
plt.savefig('images/plots/histograms/petal_width_histogram.png', bbox_inches='tight')

plt.show()

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