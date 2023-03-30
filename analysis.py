# Analysis.py
# Author: Sean Humphreys
# Script to read in and analyse the IRIS data set

# import the pandas module used to read in the data set file as a data frame
import pandas as pd
# import plotly module used to create a table of the data for display in the README.md file
import plotly.figure_factory as ff

# Define data frame as variable df to read in file 'iris.data' with a separator ',' and the column names as defined in
# the list variable called "names"
# Reference https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv - accessed 30/03/2023
df = pd.read_csv('iris.data', sep=',', names=["sepal_length_cms", "sepal_width_cms", "petal_length_cms",
                                              "petal_width_cms", "class"])

# Output a summary of each variable to a text file - https://www.statology.org/pandas-to-text-file/ accessed 30/03/2023
# variable that species path for outputting of .txt file
path = r'data_summary.txt'
# open path defined above and w to file
with open(path, 'w') as f:
    # define variable to convert the dataframe to a string, include the header and exclude the index
    df_string = df.to_string(header=True, index=False)
    # write the df_string variable to the file path
    f.write(df_string)

# ? need to remove next statements for final submission
# f = open("data_summary.txt") # validation test
# print(f.read()) # validation test
# print(df)  # validation test
# data.shape # validation test to make sure that there 150 rows of data and number of columns

# following code snippet from https://www.delftstack.com/howto/python-pandas/pandas-png/ - accessed 30/03/2023
# variable called fig to define function to create a table using plotly module for the dataframe "df"
fig = ff.create_table(df)
#  method to change the look and feel of the table
fig.update_layout(autosize=True)
# write the table_plotly.png file to the images folder
fig.write_image("images/table_plotly.png", scale=1)
