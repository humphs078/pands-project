# Analysis.py
# Author: Sean Humphreys
# Script to read in and analyse the IRIS data set

# import the pandas module used to read in the data set file as a data frame
import pandas as pd


# Define data frame as variable df to read in file 'iris.data' with a separator ',' and the column names as defined in
# the the list variable called "names"
# Reference https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv - accessed 30/03/2023
df = pd.read_csv('iris.data', sep=',', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])
print(df)  # validation test
