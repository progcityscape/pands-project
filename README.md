# pands-project
First commit [^1] consists of only the iris dataset and a test file to ensure that the link is correctly set up between the github repository and the folder on my system.

Before considering the background and history of the Iris Dataset, I would briefly like to present the following principles that will shed light on and guide our analysis of the aforementioned dataset:

* Import - First we will import the data using one of Python's built in libraries, Pandas. 
We also give the option for the user to import their own dataset (this is just to demonstrate the possibility of using other datasets - we would need significant extra program code that is outside the current scope to present the data in the same format as the Fisher Iris Dataset).  The following simple code was contained within a Try/Except block in case an invalid file\dataset was inputted:\
`FILENAME = (r'iris_data3.csv')`\
`iris = pd.read_csv(FILENAME)`
* Tidy - The advantage of using the Iris Dataset, and perhaps a reason it has been such a great tool for data scientists, is that it is already tidy - it fits the following description perfectly.  
>in a tidy dataset each row is an observation or a sample and each column is a variable.
[^2]   
* Transform - It is possible to present some basic information about the dataset, such as a summary of the variables and also their correlation, directly upon importing the data.  However to do some extra analysis, (finding the mean for each variable within each species) I found it useful to transform the data.  Realising that what I was searching for was a pivot table function, I discovered that exact replicas of many of excel's functions can be utilised with python code.\
`species_p_table = pd.pivot_table(data = iris, columns = ['species'])`
* Visualise/Model

Followed by

* Program
* Communicate

(Bullet points are adapted from _Data Analysis with the Tidyverse_)[^1].

Our analysis should begin by importing the dataset which, in this case, is Fisher’s Iris Dataset


[^1]: Data Analysis with the Tidyverse, Accessed 28 March 2023, <http://cbdm-01.zdv.uni-mainz.de/~galanisl/danalysis/>
[^2]: Pivot Tables in Pandas, Accessed 1 April 2023, <https://www.scaler.com/topics/pandas/pivot-table-pandas/>
