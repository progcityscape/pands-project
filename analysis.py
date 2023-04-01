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

# first step: load the dataset into a format that can be used by python https://datatofish.com/import-csv-file-python-using-pandas/
# leaving out path as it will not apply if the program is run from a different location

# source for iris data: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv
# 'r' is placed before the file name to deal with any special characters in the path
# adding a try/except block inspired by question on our discussion board by Sean Humphreys
# data must be read from the RAW url - https://codeigo.com/python/read-a-csv-file-from-a-url?utm_content=cmp-true - however 

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

petal_width_summary = (iris.groupby('species')['species'].count())
print (petal_width_summary)

# output the dataframe to a .txt file

with open('species_summary.txt', mode='w') as file_object:
            print(petal_width_summary, file=file_object)


