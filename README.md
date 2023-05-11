# pands-project

## Creating the Analysis File
### Import 
First we will import the data using one of Python's built in libraries, Pandas. 
We also give the option for the user to import their own dataset (this is just to demonstrate the possibility of using other datasets - we would need significant extra program code that is outside the current scope to present the data in the same format as the Fisher Iris Dataset).  The following simple code was contained within a Try/Except block in case an invalid file or dataset was inputted:\
`FILENAME = (r'iris_data3.csv')`\
`iris = pd.read_csv(FILENAME)`
### Tidy 
The advantage of using the Iris Dataset, and perhaps a reason it has been such a great tool for data scientists, is that it is already tidy - it fits the following description perfectly.  
>in a tidy dataset each row is an observation or a sample and each column is a variable. [^1]

However, I will outline later an investigation of NBA statistics, using the analysis.py file created for the Iris Dataset, that includes a dataset that requiring some tidying.
### Transform 
It is possible to present some basic information about the dataset, such as a summary of the variables and also their correlation, directly upon importing the data.  
````
var_summary = (iris.describe())
correlation = iris.corr(method='pearson')
````
However to do some extra analysis, (finding the mean for each variable within each species) I found it useful to transform the data.  Realising that what I was searching for was a pivot table function, I discovered that exact replicas of many of excel's functions can be utilised with python code.[^2]\
````
species_p_table = pd.pivot_table(data = iris, columns = [cat_var])
````
### Visualise/Model 
Using Seaborn and Matplotlib, we can create graphics that convey information about the dataset visually:
>Good data graphics will show you things that you didn’t know about the data, they will also show you things you didn’t expect, raise more questions or tell you that you’re asking the wrong questions. [^1]
In this case, I have created a selection of scatterplots and histograms that demonstrate some interesting properties of the species within the dataset.  I have divided this into a set of functions that create a chart for a given (as yet unspecified) variable:
````
def create_png(x,y):
    sns.scatterplot(x=f'{x}', y=f'{y}',
                hue=cat_var, data=iris)

    plt.savefig(f'scatter_{x}_{y}.png', bbox_inches='tight')
    # close the plot to ensure integrity of data in ensuing use
    plt.close()
    return
````
I then run each of these functions through a further function that assigns particular variables to create specific plots.\
Mathematical Models could also be created enabling us to make predictions; this is also beyond the scope of the current assignment. 


Underpinning these four principles are two further overarching ideas:

### Program 
We can use the almost limitless of capabilities of python to create analyses of our specific datasets.  An example of the extensive possibilities of python data analysis can be seen in the (unrelated) 'Iris' library that can be installed and imported - it is a 3 dimensional 'cube' that, as well as having x and y axes, has different levels.  This particular example analyses weather patterns and was originally developed by the Met Office UK.  It demonstrates that new functions and libraries can be developed within python to tackle particular problems experienced by organizations (in this case, the need to deal with the types of data particular to weather and climate.\
[Climate Data with Iris](https://ourcodingclub.github.io/tutorials/iris-python-data-vis/)
### Communicate
Having created our analysis as outlined above, it is now necessary to communicate our findings.  We have included code that will create .png files for the plots and a .txt file showing the basic analysis and summary.  These could then be used to communicate with stakeholders in any format - they could be displayed on a github page or website, or added to a powerpoint presentation, depending on the specific circumstances.  As mentioned above, I created functions both to create the plots and to assign the variables that can then be iterated to create the .png files.


(The six headings used to outline the process of creating the analysis file are adapted from _Data Analysis with the Tidyverse_)[^1].
## Extra Analysis
For some extra analysis, I have created a codeblock that filters for the categorical variable column (species) and displays a histogram showing one of the variables for a particular species.  As we will see later, the program has the ability to read in another dataset and examine for the same elements, as long as the dataset, and in particular its variables, are analagous in some way to those of the Iris Dataset.
````
        species_identify = input('Choose a specific entry from your categorical variable e.g. "setosa":' )
        num_var_identify = input('Choose a specific numerical variable to create the histogram e.g. "sepal_length:')
        # https://stackoverflow.com/questions/57297077/use-variable-in-pandas-query
        species_filter = iris.query(f'{column_heading} == @species_identify') 
        print ('Data for the histogram is taken from the following dataframe:')
        print (species_filter)
        # reuse 'histo_create()' function from earlier to create extra analysis files
        histo_create (num_var_identify, species_filter, species_identify)
````
![setosa_histogram_sepal_length](https://github.com/progcityscape/pands-project/assets/121309223/7e05c222-dcb9-4ee0-a365-a051f0ba86ec)

## 2. Fisher's Dataset
Collected by Edgar Anderson, an American botanist, the data that would eventually comprise the Iris Dataset was compiled from plants found on the Gaspe Peninsula. [^4] The eponymous biologist, Ronald A Fisher, later published the data; it contains 3 species of Iris (setosa, virginica and versicolor) with 50 samples of each, divided into 4 numerical variables (sepal length and width, petal length and width).[^5]\

The data within the dataset is both suitably concise not to overwhelm the user while also containing enough data to be able to draw meaningful conclusions and comparisons.\
## 3. Extension
Despite its tidiness, I initially found the great value of this dataset somewhat obscure.  I personally found that the best way to understand its worth was to create a comparison dataset containing data closer to my own interests; I located a set of statistics on the NBA website, specifically the season by season statistics, going back 50 years, for current champions the Golden State Warriors [(see the original stats here)](https://www.nba.com/stats/team/1610612744/seasons).  I added stats for the same time period from the LA Lakers and the Portland Trailblazers (like the 3 species of Irises - three California based basketball teams).  I then carried out the following steps on the data to prepare it for use with the analysis.py program (I used excel to prepare the CSV file due to time constraints but documented the steps to be attempted in Python at a later date):
* Converted the 'Season Column' to single years rather than a hyphenated season.
* Moved Team column to the last column to mirror the Iris Dataset (this step was later made redundant by an option in the program)
* Eliminated the Season heading as it is more of an index than a variable (year in question)
* Made copies of each tab to preserve original data
* Pasted all tabs to one sheet to combine the data into one dataset
* Got rid of win percentage, points and points rank as these all relate to the first two variables in our final dataset, which will be Games Played (GP) and  Wins (W).  I later revised this step.
* The following steps were attempts to obtain 4 usable numerical variables.
    * Got rid of all columns except Games Played, Wins, Losses and Playoff Record (left a column for Team (mirrors 'species').
    * Split Playoff Record into wins and losses and subtracted to get an an integer value showing their overall record in the post season.  Creating this integer value only for the playoffs (and not regular season wins vs losses) is an editorial decision - the playoffs are generally considered to be when the 'real' season starts and can a give a more intense and accurate picture of the team's development and can be considered a discrete variable.
    * I later decided to change the PLAYOFF RECORD to a Win percentage (take out loss and add win percentage regular season).
    * Re-import playoff record and split text to columns to get wins and losses
    * Calculated win percentage for the playoffs
    * Re-imported win percentage for the regular season.

The final CSV can be found [here](https://raw.githubusercontent.com/progcityscape/mywork/main/NBA_species%20-%20Basketball%20Species%20(2).csv), and can be loaded into the analysis.py program with options to choose the variables.

Running the CSV file through the program revealed a number of interesting contrasts with an optimum dataset such as the Iris Datset.  I had chosen to eliminate the column containing the year as I felt this would in fact create 50 different 'sub-species' within the 'species/team' column, e.g. the 2023 Golden State Warriors, the 2016 Golden State Warriors and so on.  Research revealed that this would be considered an ordinal variable and would not have strictly fit the  parameters of the Iris Dataset.  As it turned out, one of the variables I had identified as a potential numerical variable (GP: Games Played) was revealed to be uninformative, as there were only a few outliers among many records with the same value:

Figure 2: Win percentage versus Games Played

![scatter_WIN%_GP](https://github.com/progcityscape/pands-project/assets/121309223/b4adca53-d4f2-41e8-b3fb-d9dcad1071db)

This demonstrated the value of the Iris Dataset in contrast, with the consistency, spread and usability of its data.

Of more interest was the regular season record versus the playoff record (WIN% vs PLAYOFF RECORD)

Figure 3: Win Percentage versus Playoff Record

![scatter_PLAYOFF PERCENTAGE_WIN%](https://github.com/progcityscape/pands-project/assets/121309223/2c160585-b669-4ac4-9111-179b92a2fd3d)

It demonstrates that the seasons with a '0%' playoff record (either a straight loss in the first round or failure to reach the playoffs) generally (though not always) followed a poor regular season (0.2 to 0.6).  The value of a dataset such as the Iris Dataset is the linear separability - 3 Iris species with 50 samples each with one species linearly separable from the other two (the others are not linearly separable from each other)[^6].  Effectively, it is possible to draw a straight line through the objects in a linearly separable data set. [^7]

## 4. Conclusion
An extremely useful and informative dataset for data scientists, the Fisher Dataset and the accompanying development of the analysis.py file have revealed the great potential that Python has to use programming for the importing, tidying, transforming and visualising/modelling data, enabling the communication of the findings to stakeholders.  I am looking forward to building on this knowledge to explore many areas of interest with both existing datasets and those that can be developed independently. 

## Appendix A: Selected References from Coding Analysis.py
<https://www.w3schools.com/python/pandas/pandas_getting_started.asp>\
<https://realpython.com/python-histograms/>\
<https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/?ref=lbp>\
<https://datatofish.com/import-csv-file-python-using-pandas/>\
<https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv>\
<https://codeigo.com/python/read-a-csv-file-from-a-url?utm_content=cmp-true >\
<https://towardsdatascience.com/dont-download-read-datasets-with-url-in-python-8245a5eaa919>\
<https://stackoverflow.com/questions/53649222/should-i-use-with-openfile-if-i-pd-read-csv>\
<https://pythoninoffice.com/sumif-and-countif-in-pandas/#google_vignette>\
<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html>\
<https://rpubs.com/Karolina_G/848706>\
<https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm#:~:text=The%20describe()%20function%20computes,pertaining%20to%20the%20DataFrame%20columns.&text=This%20function%20gives%20the%20mean,given%20summary%20about%20numeric%20columns.>\
<https://levelup.gitconnected.com/pearson-coefficient-of-correlation-using-pandas-ca68ce678c04>\
<https://www.scaler.com/topics/pandas/pivot-table-pandas/>\
<https://stackoverflow.com/questions/1663807/how-do-i-iterate-through-two-lists-in-parallel>\
<https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/>\
<https://stackoverflow.com/questions/57297077/use-variable-in-pandas-query>\

[^1]: Data Analysis with the Tidyverse, Accessed 28 March 2023, <http://cbdm-01.zdv.uni-mainz.de/~galanisl/danalysis/>
[^2]: Pivot Tables in Pandas, Accessed 1 April 2023, <https://www.scaler.com/topics/pandas/pivot-table-pandas/>
[^3]: Unveiling the mysteries of the Iris dataset: A comprehensive analysis and Machine Learning Classification, Accessed 11 May 2023, <https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d>
[^4]: Signa, Accessed 19 March 2023, <https://wiki.irises.org/pub/Hist/Info1986SIGNA37/SIGNA_37.pdf>
[^5]: The Use of multiple measurements in taxonomic problems, Accessed 19 March 2023, <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x>
[^6]: Iris Species, Accessed 19 March 2023, <https://www.kaggle.com/datasets/uciml/iris?select=database.sqlite>
[^7]: , <https://www.baeldung.com/cs/nn-linearly-separable-data#:~:text=Linearly%20Separable%202D%20Data,than%20one%20such%20line%20exists.>
