# Analysis.py
# Author: Sean Humphreys
# Script to read in and analyse the IRIS data set

# import the pandas module used to read in the data set file as a data frame
import pandas as pd
# import plotly module used to create a table of the data for display in the README.md file
import plotly.figure_factory as ff
# import the seaborn module as sns used for plotting data representation - more advanced functionality that matplotlib
import seaborn as sns
# import the matplotlib module used to plot data for visual representation
import matplotlib.pyplot as plt
import csv

# Define data frame as variable df to read in file 'iris.data' with a separator ',' and the column names as defined in
# the list variable called "names"
# Reference https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv - accessed 30/03/2023
iris = pd.read_csv('iris.data', sep=',', names=["Sepal Length cms", "Sepal Width cms", "Petal Length cms",
                                                "Petal Width cms", "Species"])

# # # # # Check source data quality # # # # #
# The code in this section checks the quality of the source data

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
fig.update_layout(autosize=True, width=500, height=200)
# write the table_plotly.png file to the images folder
fig.write_image("images/tables/missing_values.png", scale=2)

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
sns.set_theme(context='notebook', style='darkgrid', palette='pastel', font='sans-serif', font_scale=1,
              color_codes=True, rc=None)
# code to create histograms using seaborn module - https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
# - accessed 30/03/2023
plot = sns.FacetGrid(iris, hue="Species", height=5)
# originally used distplot function but got message that it is being depreciated, when code was run, so used
# histplot function instead - https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751 - accessed 30/03/2023
plot.map(sns.histplot, "Sepal Length cms", kde=True).add_legend()
# save output to images folder - https://www.marsja.se/how-to-save-a-seaborn-plot-as-a-file-e-g-png-pdf-eps-tiff/
# - accessed 30/03/2023
plt.savefig('images/plots/histograms/sepal_length_histogram.png')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Sepal Width cms", kde=True).add_legend()
plt.savefig('images/plots/histograms/sepal_width_histogram.png')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Petal Length cms", kde=True).add_legend()
plt.savefig('images/plots/histograms/petal_length_histogram.png')

plot = sns.FacetGrid(iris, hue="Species", height=5)
plot.map(sns.histplot, "Petal Width cms", kde=True).add_legend()
plt.savefig('images/plots/histograms/petal_width_histogram.png')

plt.show()
