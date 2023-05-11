# pands-project
First commit [^1] consists of only the iris dataset and a test file to ensure that the link is correctly set up between the github repository and the folder on my system.

Before considering the background and history of the Iris Dataset, I would briefly like to present the following principles that will shed light on and guide our analysis of the aforementioned dataset:
# Creating th Analysis File
### Import 
First we will import the data using one of Python's built in libraries, Pandas. 
We also give the option for the user to import their own dataset (this is just to demonstrate the possibility of using other datasets - we would need significant extra program code that is outside the current scope to present the data in the same format as the Fisher Iris Dataset).  The following simple code was contained within a Try/Except block in case an invalid file or dataset was inputted:\
`FILENAME = (r'iris_data3.csv')`\
`iris = pd.read_csv(FILENAME)`
### Tidy 
The advantage of using the Iris Dataset, and perhaps a reason it has been such a great tool for data scientists, is that it is already tidy - it fits the following description perfectly.  
>in a tidy dataset each row is an observation or a sample and each column is a variable. [^1]

### Transform 
It is possible to present some basic information about the dataset, such as a summary of the variables and also their correlation, directly upon importing the data.  However to do some extra analysis, (finding the mean for each variable within each species) I found it useful to transform the data.  Realising that what I was searching for was a pivot table function, I discovered that exact replicas of many of excel's functions can be utilised with python code.[^2]\
`species_p_table = pd.pivot_table(data = iris, columns = ['species'])`
### Visualise/Model 
Using Seaborn and Matplotlib, we can create graphics that convey information about the dataset visually:
>Good data graphics will show you things that you didn’t know about the data, they will also show you things you didn’t expect, raise more questions or tell you that you’re asking the wrong questions. [^1]
In this case, we have created a selection of scatterplots and histograms that demonstrate some interesting properties of the species within the dataset.  I have divided this into a set of functions that create a chart for a given (as yet unspecified) variable:

`def create_png_width(x,y):`\
`    sns.scatterplot(x=f'{x}_width', y=f'{y}_width',`\
`               hue='species', data=iris)`
  
I then run each of these functions through a further function that assigns particular variables to create specific plots.\
Mathematical Models could also be created enabling us to make predictions; this is also beyond the scope of the current assignment. 


Underpinning these four principles are two further overarching ideas:

### Program 
We can use the almost limitless of capabilities of python to create analyses of our specific datasets.  An example of the extensive possibilities of python data analysis can be seen in the (unrelated) 'Iris' library that can be installed and imported - it is a 3 dimensional 'cube' that, as well as having x and y axes, has different levels.  This particular example analyses weather patterns and was originally developed by the Met Office UK.  It demonstrates that new functions and libraries can be developed within python to tackle particular problems experienced by organizations (in this case, the need to deal with the types of data particular to weather and climate.\
[Climate Data with Iris](https://ourcodingclub.github.io/tutorials/iris-python-data-vis/)
### Communicate
Having created our analysis as outlined above, it is now necessary to communicate our findings.  We have included code that will create .png files for the plots and a .txt file showing the basic analysis and summary.  These could then be used to communicate with stakeholders in any format - they could be displayed on a github page or website, or added to a powerpoint presentation, depending on the specific circumstances.  As mentioned above, I created functions both to create the plots and to assign the variables that can then be iterated to create the .png files

(The six headings used to outline the process of creating the analysis file are adapted from _Data Analysis with the Tidyverse_)[^1].

Our analysis should begin by importing the dataset which, in this case, is Fisher’s Iris Dataset


[^1]: Data Analysis with the Tidyverse, Accessed 28 March 2023, <http://cbdm-01.zdv.uni-mainz.de/~galanisl/danalysis/>
[^2]: Pivot Tables in Pandas, Accessed 1 April 2023, <https://www.scaler.com/topics/pandas/pivot-table-pandas/>
