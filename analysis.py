# Write a program called analysis.py that:
# 1. Outputs a summary of each variable to a single text file,
# 2. Saves a histogram of each variable to png files, and
# 3. Outputs a scatter plot of each pair of variables.
# 4. Performs any other analysis you think is appropriate
# author: john kelleher

# first step is to import the pandas library https://www.w3schools.com/python/pandas/pandas_getting_started.asp
# also importing numpy
import pandas as pd
import numpy as np

# we will need visualization packages as well - Seaborn and MatPlotLib
import seaborn as sns
import matplotlib.pyplot as plt

# first step: load the dataset into a format that can be used by python https://datatofish.com/import-csv-file-python-using-pandas/
# leaving out path, as it will not apply if the program is run from a different location.

# source for iris data: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv
# 'r' is placed before the file name to deal with any special characters in the path
# adding a try/except block inspired by question on our discussion board by Sean Humphreys
# data must be read from the RAW url - https://codeigo.com/python/read-a-csv-file-from-a-url?utm_content=cmp-true 
# https://towardsdatascience.com/dont-download-read-datasets-with-url-in-python-8245a5eaa919 

'''
url = r'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
'''
FILENAME = input("Please input your URL here. \nTo use the Iris Dataset please press enter: ")

# exception in case the file is moved/deleted from the online source
# discovered that with/open is not needed when working with pandas as it handles files differently
# https://stackoverflow.com/questions/53649222/should-i-use-with-openfile-if-i-pd-read-csv

try:
    iris = pd.read_csv(FILENAME)
   
except:
    FILENAME = (r'iris_data3.csv')
    iris = pd.read_csv(FILENAME)

# find the total amount of samples by species
# https://pythoninoffice.com/sumif-and-countif-in-pandas/#google_vignette shows us how to count and sum by variable as well as other functions, such as mean
# difficult to get the total number of species without it returning a table of columns
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html


species_type_summary = (iris.groupby('species')['species'].count())

# Create a summary of the variables.
# https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm#:~:text=The%20describe()%20function%20computes,pertaining%20to%20the%20DataFrame%20columns.&text=This%20function%20gives%20the%20mean,given%20summary%20about%20numeric%20columns.

var_summary = (iris.describe())


# find correlation between the columns - https://levelup.gitconnected.com/pearson-coefficient-of-correlation-using-pandas-ca68ce678c04
correlation = iris.corr(method='pearson')

# I'm going to play around with pandas 'pivot_table' function to see if we can rearrange the dataframe
# https://www.scaler.com/topics/pandas/pivot-table-pandas/
# the dataframe will now show the mean for each variable vs. species

species_p_table = pd.pivot_table(data = iris,
                            columns = ['species'])
                            
# output the dataframes to a .txt file
with open('species_summary.txt', mode='w') as file_object:
            print (f'Samples Per Type:\n{species_type_summary}\n\nSummary of Variables:\n{var_summary}\n' , file=file_object)
            print (f'Correlation:\n{correlation}\n', file = file_object)
            print (f'Extra Analysis: \nPivot Table - Mean for each variable per species:\n{species_p_table}\n', file = file_object)
# https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ - exploring ways to create plots
# https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib - used this to work out why the second png was saving with 6 species (doubling up on the original 3).
# decided to create a function to create the png files by using different combinations of the variables 
# (assignment asked for each pair so assuming this is not limited to sepal/sepal and petal/petal)
# the following code block is unwieldy and could be made much more efficient - need to research how to do this.
# this function creates png files for combinations of variables with differing dimensions (e.g. length v width)


def create_png(x,y):
    sns.scatterplot(x=f'{x}_length', y=f'{y}_width',
                hue='species', data=iris)

    plt.savefig(f'scatter_{x}_{y}.png', bbox_inches='tight')
    # close the plot to ensure integrity of data in ensuing use
    plt.close()
    return


# this function creates png files for combinations of variables with the same dimensions (e.g. length v length)


def create_png_length(x,y):
    sns.scatterplot(x=f'{x}_length', y=f'{y}_length',
                hue='species', data=iris)

    plt.savefig(f'scatter_{x}_{y}_length.png', bbox_inches='tight')
    plt.close()
    return


# this function creates png files for combinations of variables with the same dimensions (e.g. width v width)


def create_png_width(x,y):
    sns.scatterplot(x=f'{x}_width', y=f'{y}_width',
                hue='species', data=iris)

    plt.savefig(f'scatter_{x}_{y}_width.png', bbox_inches='tight')
    plt.close()
    return


# create a function to assign different variable names and include the previous function


def variable_names(var1, var2):
    create_png(var1,var2)
    return


# this is an inefficient solution to include occasions when the variables are of the same dimension, e.g. sepal_length vs petal_length


def variable_names_2(var1, var2):
    create_png_length(var1,var2)
    create_png_width(var1,var2)
    return


# it would be useful to create a loop instead of this block of code
a = ('sepal')
b = ('petal')

# run the functions
variable_names(a,b)
variable_names(a,a)
variable_names(b,b)
variable_names(b,a)
variable_names_2(a,b)
variable_names_2(b,a)

# project description asks for a 'histogram of each variable' - what does this mean?
# the following code creates a histogram for each
# https://realpython.com/python-histograms/
# https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/?ref=lbp
# used the code provided at the above link to create a function that will output to a .png file for each of the variables


def histogram_var (variable, dimension):
    plt.figure(figsize = (10,7))
    x = iris[f"{variable}_{dimension}"]
    plt.hist(x, bins = 20, color = "green")
    plt.title(f"{variable} {dimension} in cm")
    plt.xlabel(f"{variable}_{dimension}")
    plt.ylabel("Count")
    plt.savefig(f'histogram_{variable}_{dimension}.png', bbox_inches='tight')
    plt.close
    return


# run the function for each combination of variable and dimension e.g. sepal width


histogram_var(a, "width")
histogram_var(a, "length")
histogram_var(b, "width")
histogram_var(b, "length")


# next we will do some additional analysis on the dataset

