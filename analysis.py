# Analysis.py
# Author: Sean Humphreys
# Script to read in and analyse the IRIS data set. The location of the data is defined in the url variable in line XX
# of the script. The output of the script is saved to a folder called "script_output" in the home directory on the
# machine on which the script is run. This allows for portability of the script between different machines and OS's. If
# the directory does not exist the script will create the directory. The output to the "script_output" folder consists
# af a number of tables and graphs. The tables will give a summary of the dataset and the plots demonstrate univariate,
# bivariate and multivariate analysis on the dataset. A file called "data_summary.txt" is created that gives a summary
# of the dataset variables. The script prints a series of updates to let the user know that the script is working. The
# script does not show or open any of the tables or plots.

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
# import the csv library
import csv
# import the nummpy package as np
import numpy as np
# import the OS library needed for checking, creation and deletion of files and folders
import os
# import the earthpy packages used to check the home directory
import earthpy as et
# time library used to save files with current date & time stamp in filename
import datetime

# # # # # Declare Global Variables # # # # #
# declare a variable to define the Iris Data Set URL

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# define timestamp for output filenames
# https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python
# - accessed 23/04/2023
time_stamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')


# https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/work-with-files-directories-paths-in-python/set-working-directory-os-package/
# accessed 23/04/2023
# define a variable to the "script_output" folder in the home directory of the os
script_output_folder = os.path.join(et.io.HOME, "script_output")

# # # # # Define Functions # # # # #
# ? need to remove if no functions
# possible functions - function to save tables from dataframe -

# # # # # Set Themes # # # # #

# Set Seaborn theme to use pastel colours

# https://seaborn.pydata.org/generated/seaborn.set_theme.html - accessed 20/04/2023
sns.set_theme(context='notebook', style='white', palette='pastel', font='sans-serif', font_scale=1, color_codes=True,
              rc=None)

# # # # # Create "script_output" folder # # # # #

# code in this section is based on tutorial found here -
# https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/work-with-files-directories-paths-in-python/set-working-directory-os-package/
# accessed 23/04/2023

# if statement to check if the "script_output" folder exists. If not create the folder in the users home directory. If
# the folder exists and the method tries to create it and error will be thrown so only create folder if it doesn't exist
if os.path.exists(script_output_folder) != True:
    os.mkdir(script_output_folder)

# # # # # Read in the data set set from URL # # # # #

print("Reading in the Iris Data Set as a dataframe..........")
# Define data frame as variable iris. Use Pandas to read in file from the URL variable with the column names as defined
# in the list = "names"
# Reference https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv - accessed 30/03/2023

iris = pd.read_csv(url, names=["Sepal Length cms", "Sepal Width cms", "Petal Length cms", "Petal Width cms", "Species"])
# print(iris) # validation check ? remove
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

# following code snippet from
# https://www.delftstack.com/howto/python-pandas/pandas-png/#convert-pandas-dataframe-table-into-png-image-with-plotly-and-kaleido
# - accessed 30/03/2023

# declare a variable for the ff.create table method
fig = ff.create_table(missing_values_table_csv)
#  method to change the look and feel of the table
fig.update_layout(autosize=False, width=300, height=200)
# write the table_plotly.png file to the images folder
fig.write_image(f"{script_output_folder}/missing_data_summary_{time_stamp}.png", scale=1)

# Delete CSV files no longer needed - https://www.geeksforgeeks.org/python-os-remove-method/ - accessed 22/04/2023
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
# adding header - https://stackoverflow.com/questions/51463449/replace-csv-header-without-deleting-the-other-rows
# accessed 22/04/2023
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
fig_2 = ff.create_table(data_summary)
#  method to change the look and feel of the table
fig_2.update_layout(autosize=False, width=700, height=200)
# write the table_plotly.png file to the images folder
fig_2.write_image(f"{script_output_folder}/data_summary_{time_stamp}.png", scale=1)

# Clean up unnecessary files
os.remove("output.csv")

# Clean up unnecessary files
os.remove("summary_stats.csv")

print(f"Data summary table complete. Output saved to \"script_output\" folder as data_summary.png")

# # # # # Create summary table of data for appendix 1 # # # # #

print('Creating a summary table of full data set..........')

# variable called fig to define function to create a table using plotly module for the dataframe "df"
fig_3 = ff.create_table(iris)
#  method to change the look and feel of the table
fig_3.update_layout(autosize=True)
# write the table_plotly.png file to the images folder
fig_3.write_image(f"{script_output_folder}/full_data_set_table_{time_stamp}.png", scale=1)

print(f"Full data set summary table complete. Output saved to \"script_output\" folder as full_data_set_table.png")

# # # # # Create & save histograms # # # # #

print('Creating histograms analysis of the data set..........')

# code to create histograms using seaborn module - https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
# - accessed 30/03/2023
plot = sns.FacetGrid(iris, hue="Species", height=6)
# originally used distplot function but got message that it is being depreciated, when code was run, so used
# histplot function instead - https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751 - accessed 30/03/2023
plot.map(sns.histplot, "Sepal Length cms", kde=True).set(title='Sepal Length Distribution')  # add a title to the plot
# https://www.statology.org/seaborn-title/ - accessed 22/04/2023
plt.legend()
# save output to images folder - https://www.marsja.se/how-to-save-a-seaborn-plot-as-a-file-e-g-png-pdf-eps-tiff/
# - accessed 30/03/2023
plt.savefig(f'{script_output_folder}/sepal_length_histogram_{time_stamp}.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=6)
plot.map(sns.histplot, "Sepal Width cms", kde=True).set(title='Sepal Width Distribution')
plt.legend()
# prevent the title from being cut off the saved plot
# https://stackoverflow.com/questions/35992492/savefig-cuts-off-title - accessed 22/04/2023
plt.savefig(f'{script_output_folder}/sepal_width_histogram_{time_stamp}.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=6)
plot.map(sns.histplot, "Petal Length cms", kde=True).set(title='Petal Length Distribution')
plt.legend()
plt.savefig(f'{script_output_folder}/petal_length_histogram_{time_stamp}.png', bbox_inches='tight')

plot = sns.FacetGrid(iris, hue="Species", height=6)
plot.map(sns.histplot, "Petal Width cms", kde=True).set(title='Petal Width Distribution')
plt.legend()
plt.savefig(f'{script_output_folder}/petal_width_histogram_{time_stamp}.png', bbox_inches='tight')
plt.close()  # https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it accessed
# 20/04/2023
print('Histograms have been saved in the \"script_output\" folder')

# # # # # Create & save box plots # # # # #

# Reference - https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

print('Creating box plots..........')

# function to pass arguments to sns.boxplot method

def graph(y):
    sns.boxplot(x="Species", y=y, data=iris)


# plot size
plt.figure(figsize=(10, 10))
plt.suptitle('Iris Data Set Box Plots', size=15)  # add a title https://matplotlib.org/stable/api/figure_api.html
# - accessed 20/04/2023

# Adding the subplot at the specified grid position
plt.subplot(221)
graph('Sepal Length cms')

plt.subplot(222)
graph('Sepal Width cms')

plt.subplot(223)
graph('Petal Length cms')

plt.subplot(224)
graph('Petal Width cms')


# Save plot to file
plt.savefig(f'{script_output_folder}/box_plots_{time_stamp}.png')
plt.close()

print('Boxplots have been saved in the \"script_output\" folder')

# # # # # Outliers Demo # # # # #

print('Demonstrating outliers..........')

# create a deep copy of the original Iris dataframe - https://www.w3schools.com/python/pandas/ref_df_copy.asp
outlier_test = iris.copy()

# remove all rows so that only Iris-setosa remains
# https://www.shanelynn.ie/pandas-drop-delete-dataframe-rows-columns/ - accessed 10/04/2023
outlier_test.drop(index=outlier_test.index[50:150], axis=0, inplace=True)

# plot the boxplot demonstrating outliers
sns.boxplot(x="Species", y="Petal Length cms", data=outlier_test).set_title("Petal Length Outliers")
plt.ylim(0.75, 2)  # https://stackoverflow.com/questions/33227473/how-to-set-the-range-of-y-axis-for-a-seaborn-boxplot
# accessed 20/04/2023
plt.legend([],[], frameon=False)  # the leged was showing on the plot, to get rid of it solution found here -
# https://www.delftstack.com/howto/seaborn/remove-legend-seaborn-plot/ accessed 20/04/2023
plt.savefig(f'{script_output_folder}/outliers_box_plots_{time_stamp}.png', bbox_inches='tight')
plt.close()

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
plt.ylim(.75, 2)
plt.legend([],[], frameon=False)
plt.savefig(f'{script_output_folder}/no_outliers_box_plots_{time_stamp}.png', bbox_inches='tight')
plt.close()

print('Outlier demonstration has been saved to \"script_output\" folder')

# # # # # Violin PLots # # # # #
# based on code found here -
# https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40
# accessed 22/04/2023

print('Creating violin plots..........')


def violin_graph(y):
    sns.violinplot(x="Species", y=y, data=iris)


# plot size
plt.figure(figsize=(10, 10))
plt.suptitle('The Iris Data Set Violin Plots')  # Add title to plot
# Adding the subplot at the specified grid position
plt.subplot(221)
violin_graph('Sepal Length cms')

plt.subplot(222)
violin_graph('Sepal Width cms')

plt.subplot(223)
violin_graph('Petal Length cms')

plt.subplot(224)
violin_graph('Petal Width cms')

plt.savefig(f'{script_output_folder}/violin_plots_{time_stamp}.png')
plt.close()

print('Violin plots have been saved to the \"script_output\" folder')

# # # # # Generate Heatmap # # # # #

print('Creating data set heatmap..........')

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

plt.savefig(f'{script_output_folder}/heatmap_{time_stamp}.png', bbox_inches='tight')
plt.close()

print('Heatmap has been saved to the \"script_output\" folder')

# # # # # Create Pairplot # # # # #

print("Creating pairplots..........")

# Pairplots based on code at - http://uconn.science/wp-content/uploads/2017/07/iris_visualization.html - accessed
# 22/04/2023

# Create the pairplot with Kernel Density Estimation as opposed histograms in the diagonal elements
# Title format found here -
# https://www.tutorialspoint.com/how-to-show-the-title-for-the-diagram-of-seaborn-pairplot-or-pridgrid-matplotlib
# accessed 20/04/2023
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
sns.pairplot(iris, hue="Species", height=3.5, diag_kind="kde").fig.suptitle("Iris Data Set Pairplot")
plt.savefig(f'{script_output_folder}/pairplot_{time_stamp}.png',bbox_inches='tight')
plt.close()

print('Pairplots saved to the \"script_output\" folder')

# # # # # Andrews Curves # # # # #

print('Creating Andrew\'s curves..........')
# issue with format of chart - use following method to clear the format -
# https://www.tutorialspoint.com/how-to-clear-the-memory-completely-of-all-matplotlib-plots - accessed 20/04/2023
plt.figure().clear()

# code from - http://uconn.science/wp-content/uploads/2017/07/iris_visualization.html#Andrews-Curves
andrews_curves(iris, "Species").set(title='Iris Data Set Andrew\'s Curves')
plt.savefig(f'{script_output_folder}/andrews_curves_{time_stamp}.png', bbox_inches='tight')
plt.close()

print('Andrew\'s Curves plot saved to the \"script_output\" folder')

# # # # # Parallel Coordinates # # # # #

print('Creating parallel coordinates plot..........')
plt.figure().clear()
# code from - http://uconn.science/wp-content/uploads/2017/07/iris_visualization.html#parallel_coordinates
parallel_coordinates(iris, "Species").set(title='Iris Data Set Parallel Coordinates')
plt.savefig(f'{script_output_folder}/parallel_coordinates_{time_stamp}.png', bbox_inches='tight')
plt.close()

print('Parallel coordinates plot saved to \"script_output\" folder')

# # # # # RadViz # # # # #

print('Creating radviz plot..........')
plt.figure().clear()
# code frm - http://uconn.science/wp-content/uploads/2017/07/iris_visualization.html#radviz
radviz(iris, "Species").set(title='Iris Data Set Radviz')
plt.savefig(f'{script_output_folder}/radviz_{time_stamp}.png', bbox_inches='tight')
plt.close()

print('Parallel coordinates plot saved to \"script_output\" folder')

# # # # # Lag Plot # # # # #

print('Creating Lag Plot..........')

sns.reset_defaults()

# code from - https://towardsdatascience.com/6-lesser-known-pandas-plotting-tools-fda5adb232ef
iris.drop('Species', axis=1, inplace=True)
plt.figure(figsize=(10,6))
lag_plot(iris).set(title='Iris Data Set Lag Plot')
plt.savefig(f'{script_output_folder}/lag_plot_{time_stamp}.png', bbox_inches='tight')
plt.close()

print('Lag plot saved to \"script_output\" folder')

print(f'\nThe script has completed successfully. All tables and plots have been saved in the "{script_output_folder}" '
      f'folder.')