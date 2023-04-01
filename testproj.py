import pandas as pd

FILENAME = r'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

with open (FILENAME) as my_file:  
    # no headings included in csv file - https://github.com/rasbt/python-machine-learning-book-2nd-edition/issues/69
  
    iris = pd.read_csv(my_file)

print (iris)

with open("hello.txt") as my_file:
    print(my_file.read())