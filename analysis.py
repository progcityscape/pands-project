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
# leaving out path as it will not apply if the program is run from a different location

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

finally:
    print (iris)


# find the total amount of samples by species
# https://pythoninoffice.com/sumif-and-countif-in-pandas/#google_vignette shows us how to count and sum by variable as well as other functions, such as mean
# difficult to get the total number of species without it returning a table of columns
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html


species_type_summary = (iris.groupby('species')['species'].count())

# Create a summary of the variables.
# https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm#:~:text=The%20describe()%20function%20computes,pertaining%20to%20the%20DataFrame%20columns.&text=This%20function%20gives%20the%20mean,given%20summary%20about%20numeric%20columns.

var_summary = (iris.describe())


### not documented
correlation = iris.corr(method='pearson')

# output the dataframe to a .txt file

with open('species_summary.txt', mode='w') as file_object:
            print (f'Samples Per Type:\n{species_type_summary}\n\nSummary of Variables:\n{var_summary}\n' , file=file_object)
            print (f'Correlation:\n{correlation}', file = file_object)

# https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ - exploring ways to create plots
# https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib - used this to work out why the second png was saving with 6 species (doubling up on the original 3).

sns.countplot(x='species', data=iris)
plt.show()
plt.close()

plt.hist(iris['species'])
plt.show()
plt.close()
# the following was the original code to create the scatterplots
'''
sns.scatterplot(x='sepal_length', y='sepal_width',
                hue='species', data=iris)

plt.savefig('scatter_sepal.png', bbox_inches='tight')
plt.close()


sns.scatterplot(x='petal_length', y='petal_width',
                hue='species', data=iris)

plt.savefig('scatter_petal.png', bbox_inches='tight')
plt.close()
'''
# creating a function to create the png files by using different combinations of the variables 
# (assignment asked for each pair so assuming this is not limited to sepal/sepal and petal/petal)

def create_png(x,y):
    sns.scatterplot(x=f'{x}_length', y=f'{y}_width',
                hue='species', data=iris)

    plt.savefig(f'scatter_{x}_{y}.png', bbox_inches='tight')
    # close the plot to ensure integrity of data in ensuing use
    plt.close()
    return

def create_png_length(x,y):
    sns.scatterplot(x=f'{x}_length', y=f'{y}_length',
                hue='species', data=iris)

    plt.savefig(f'scatter_{x}_{y}_length.png', bbox_inches='tight')
    plt.close()
    return

def create_png_width(x,y):
    sns.scatterplot(x=f'{x}_width', y=f'{y}_width',
                hue='species', data=iris)

    plt.savefig(f'scatter_{x}_{y}_width.png', bbox_inches='tight')
    # close the plot to ensure integrity of data in ensuing use
    plt.close()
    return

# create a function to assign different variable names and include the previous function
def variable_names(var1, var2):
    create_png(var1,var2)
    return

# this is an inefficient solution to include when the variables are for example sepal_length vs petal_length
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



