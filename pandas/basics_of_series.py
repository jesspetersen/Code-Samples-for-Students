# Import pandas and check the version

import pandas as pd
print(pd.__version__)
print(pd.show_versions(as_json=True))

# Create a series from a list, numpy array and dict.
import numpy as np  # importing numpy

# creating lists and dictionaries
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr)) 

# Creating series objects
ser2 = pd.Series(mylist)
ser1 = pd.Series(myarr)
ser3 = pd.Series(mydict)
print(ser3.head()) # .head() gives the first 5 rows of any dataframe or series

## Assign name to the series' index
ser2.name = 'alphabet'
print(ser2.head()) # print first 5 rows of ser2




## Series functionality

ser1.head() # gives the first 5 rows of series 'ser1'

ser1.tail() # gives the last 5 rows of series 'ser1'

ser1.min() # gives minimum value in ser1

ser1.max() # returns max value

ser1.unique() # returns an array of unique values in ser1




### Series Math

ser1.mean() # returns mean value of the elements in the series 'ser1'

ser1.mode() # gives mode value

ser1.median() # returns median value

ser1[21:25] # Similar to list slicing, this gives the elements having indices 21 to 24 ('Note' : Last index is excluded). 

ser1[21:25].mean() # return mean value of the sliced series


