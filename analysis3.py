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
# I will define all the required functions in this block and then use them later in the program.
# This function groups the variables into a usable form

def summary_create(cat_var):
        species_type_summary = (iris.groupby(cat_var)[cat_var].count())
        return species_type_summary

# This function creates a scatterplot based on the headings specified by the user (specified in later codeblock)

def create_png(x,y):
    sns.scatterplot(x=f'{x}', y=f'{y}',
                hue=cat_var, data=iris)

    plt.savefig(f'scatter_{x}_{y}.png', bbox_inches='tight')
    # close the plot to ensure integrity of data in ensuing use
    plt.close()
    return

# This function creates histograms based on the specified variables.
# project description asks for a 'histogram of each variable' - what does this mean? I will initially create histograms for each variable with some extension in the extra analysis.
# the following code creates a histogram for each
# https://realpython.com/python-histograms/
# https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/?ref=lbp
# used the code provided at the above link to create a function that will output to a .png file for each of the variables

def histo_create(i, dataframe_1):
        print (f'Creating .png {i}')
        plt.figure(figsize = (10,7))
        x = dataframe_1[f'{i}']
        plt.hist(x, bins = 20, color = "green")
        plt.title(f"{i} in cm")
        plt.xlabel(f"{i}")
        plt.ylabel("Count")
        plt.savefig(f'histogram_{i}.png', bbox_inches='tight')
        plt.close
        return

# first step: load the dataset into a format that can be used by python https://datatofish.com/import-csv-file-python-using-pandas/
# leaving out path, as it will not apply if the program is run from a different location.
# source for iris data: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv
# 'r' is placed before the file name to deal with any special characters in the path
# adding a try/except block inspired by question on our discussion board by Sean Humphreys
# data must be read from the RAW url - https://codeigo.com/python/read-a-csv-file-from-a-url?utm_content=cmp-true 
# https://towardsdatascience.com/dont-download-read-datasets-with-url-in-python-8245a5eaa919 
FILENAME = input("Please input your URL here. \nTo use the Iris Dataset please press enter: ")
# exception in case the user does not want to enter their own online csv source
# discovered that with/open is not needed when working with pandas as it handles files differently
# https://stackoverflow.com/questions/53649222/should-i-use-with-openfile-if-i-pd-read-csv
try:
    iris = pd.read_csv(FILENAME)
    # in this section of the program we will ask the user to specify the headings to be used (4 numerical variables and one categorical variable)
    cat_var = input("What is your categorical variable? (press enter to accept the default):")
    species_type_summary = (summary_create(cat_var))
    num_var1 = input("What is your first numerical variable? (case sensitive):")
    num_var2 = input("What is your second numerical variable? (case sensitive):")
    num_var3 = input("What is your third numerical variable? (case sensitive):")
    num_var4 = input("What is your fourth numerical variable? (case sensitive):")

except:
    # this exception allows the user to use the default option (the Iris Dataset).
    FILENAME = (r'iris_data3.csv')
    iris = pd.read_csv(FILENAME)
    # need to specify the variables if the iris dataset is being used
 
    # find the total amount of samples by species
    # https://pythoninoffice.com/sumif-and-countif-in-pandas/#google_vignette shows us how to count and sum by variable as well as other functions, such as mean
    # difficult to get the total number of species without it returning a table of columns
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
    # Will create a function that allows you to choose your own categorical variable depending on your dataset.
    # https://rpubs.com/Karolina_G/848706 explains that the 'species' variable is a categorical variable.

    # In the following section, I have attempted to generalize the program to incorporate a different dataset (it still needs to have 3 numerical and one categorical variables).
    # In honour of the Iris Dataset, I have retained 'species' in the variable names and 'iris' as the dataframe name (also becuase there are so many instances of the name in the first program draft).
    cat_var = 'species'
    species_type_summary = (summary_create(cat_var)) 
    num_var1 = ('sepal_length')
    num_var2 = ('sepal_width')
    num_var3 = ('petal_length')
    num_var4 = ('petal_width')

 
# Create a summary of the variables.
# https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm#:~:text=The%20describe()%20function%20computes,pertaining%20to%20the%20DataFrame%20columns.&text=This%20function%20gives%20the%20mean,given%20summary%20about%20numeric%20columns.
var_summary = (iris.describe())
# find correlation between the columns - https://levelup.gitconnected.com/pearson-coefficient-of-correlation-using-pandas-ca68ce678c04
correlation = iris.corr(method='pearson')
# I'm going to play around with pandas 'pivot_table' function to see if we can rearrange the dataframe
# https://www.scaler.com/topics/pandas/pivot-table-pandas/
# the dataframe will now show the mean for each variable vs. species
species_p_table = pd.pivot_table(data = iris, columns = [cat_var])
# output the dataframes to a .txt file
# in this new version of the program I use the categorical variable inputted earlier to title the text file.
with open(f'{cat_var}_summary.txt', mode='w') as file_object:
            print (f'Samples Per Type:\n{species_type_summary}\n\nSummary of Variables:\n{var_summary}\n' , file=file_object)
            print (f'Correlation:\n{correlation}\n', file = file_object)
            print (f'Extra Analysis: \nPivot Table - Mean for each variable per {cat_var}:\n{species_p_table}\n', file = file_object)

# the following function will print .png files of the scatterplots, based on inputted user headings.
# we need to create a scatterplot for each pair of variables so iterating through two tuples should work.
# https://stackoverflow.com/questions/1663807/how-do-i-iterate-through-two-lists-in-parallel

num_var_list = [num_var1, num_var2, num_var3, num_var4, num_var1, num_var2]
num_var_list2 = [num_var2, num_var3, num_var4, num_var1, num_var3, num_var4]

for (i,j) in zip(num_var_list, num_var_list2): 
    print (i, j)
    # the following code will create the .png within the for loop
    sns.scatterplot(x=f'{i}', y=f'{j}',
                hue=cat_var, data=iris)

    plt.savefig(f'scatter_{i}_{j}.png', bbox_inches='tight')
    # close the plot to ensure integrity of data in ensuing use
    # see comments below for references/ sources for this code
    plt.close()

for k in num_var_list:
    histo_create(k, iris)        
'''
for i in num_var_list: 
    print (f'Creating .png {i}')
    plt.figure(figsize = (10,7))
    x = iris[f'{i}']
    plt.hist(x, bins = 20, color = "green")
    plt.title(f"{i} in cm")
    plt.xlabel(f"{i}")
    plt.ylabel("Count")
    plt.savefig(f'histogram_{i}.png', bbox_inches='tight')
    plt.close
'''
# With the main ponts of the program complete, it would be interesting to see a histogram per species, e.g. 'setosa' 'petal_length'
# We will give the user options to do an extra analysis using try and except, and we will use the histogram function 'histo_create()'.
# dataframe versus dataframe name causing problem reusing the histo_create function - may be overwriting existing png files.
'''
print (num_var1, num_var2, num_var3, num_var4)
print (species_p_table)
'''

species_filter = iris.query('species == "setosa"') 
print (species_filter)

histo_create (num_var1, species_filter)

'''
& carrier == "B6"')
'''

