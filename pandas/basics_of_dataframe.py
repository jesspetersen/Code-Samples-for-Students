import pandas as pd # Import pandas library as pd

example_dict = {'Name' : ['Jahnavi', 'Chitta'], 'Address' : ['Hyderabad', 'Vijayawada']} # Creating example dictionary

example_dataframe = pd.DataFrame(example_dict) # .DataFrame() function converts a dictionary into dataframe

print('Example_Dataframe')
print(example_dataframe)




## Combine many series to form a dataframe

import numpy as np # Import numpy module as np
# Create 2 series
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz')) # Returns series of alphabets from 'a' to 'z'
ser2 = pd.Series(np.arange(26)) # Returns series of numbers from 0 to 25

# Create dataframe using 2 series 'ser1' and 'ser2'
# Method 1
df = pd.concat([ser1, ser2], axis=1) # .concat() gives the concated version of series, i.e, a dataframe

# Method 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2}) # .DataFrame() function gives dataframe of the choosen series, with col names.
print('\nDataframe using 2 series')
print('\nDataframe head')
print(df.head())  # gives first 5 rows of dataframe

print('\nDataframe tail')
print(df.tail(10)) # Returns last 10 rows of the dataframe 'df'

## Dataframe Functionality

print('\nShape of df')
print(df.shape) # Gives the shape of dataframe in (rows, columns) format.

# The describe() function
print('\nSummary Statistics of df')
print(df.describe()) # This is the most important yet basic function. This displays the summary statistics of each variable column wise.

print('\nMinimum of df')
print(df.min()) # Gives min value element in columns of df

print('\nMaximum of df')
print(df.max()) # Gives max value element in columns of df

