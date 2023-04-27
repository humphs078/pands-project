# functions.py
# Author: Sean Humphreys
# File that contains functions created for use in Iris Data Set Analysis

# following code snippet from
# https://www.delftstack.com/howto/python-pandas/pandas-png/#convert-pandas-dataframe-table-into-png-image-with-plotly-and-kaleido
# - accessed 30/03/2023

# create a function. Argument "file" is the input file path. Argument "output_file" is th output file path.
def table_save(file, output_file):
    import plotly.figure_factory as ff  # this function doesn't work unless the module is imported as part of the
    # function - ff is not recognised if the module is imported in the file where the function is imported too
    # declare a variable for the ff.create table method
    fig = ff.create_table(file)
    #  method to change the look and feel of the table
    fig.update_layout(autosize=True)
    # write the table_plotly.png file to the images folder
    fig.write_image(output_file, scale=1)


# test function - execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
# https://realpython.com/if-name-main-python/ accessed 27/04/2023
if __name__ == "__main__":

    # import the pandas module used to read in the data set file as a data frame
    import pandas as pd
    # import plotly module used to create a table of the data for display in the README.md file
    #import plotly.figure_factory as ff
    # import the csv library used for csv file reading and writing
    import csv
    # import the OS library needed for checking, creation and deletion of files and folders
    import os
    # import the earthpy packages used to check the home directory
    import earthpy as et
    # time library used to save files with current date & time stamp in filename
    import datetime

    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

    iris = pd.read_csv(url, names=["Sepal Length cms", "Sepal Width cms", "Petal Length cms",
                                   "Petal Width cms", "Species"])

    script_output_folder = os.path.join(et.io.HOME, "script_output")
    # if statement to check if the "script_output" folder exists. If not create the folder in the users home
    # directory. If the folder exists and the method tries to create it an error will be thrown so only create folder
    # if it doesn't exist
    if not os.path.exists(script_output_folder):
        os.mkdir(script_output_folder)

    # The code in this section checks the quality of the source data and writes the output to a table. To achieve
    # this the isnull() method is used and transposed to a CSV. Headers are injected into the CSV to make it
    # understandable. The CSV is read in as a dataframe and a table based on the dataframe is then saved to file.
    # This is a roundabout way however it was the only way to be found to create a table with presentable formatting

    # Define a variable to use the check for missing data using the isnull() method
    # https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
    missing_values_table = iris.isnull().sum().T
    # Transpose the table to a csv file
    missing_values_table.transpose().to_csv('missing_values.csv', sep=',')

    # define headers for the csv file
    header = ['Column', 'Missing Values']
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
    time_stamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')

    table_save(missing_values_table_csv, f"{script_output_folder}/missing_data_summary_{time_stamp}.png")
