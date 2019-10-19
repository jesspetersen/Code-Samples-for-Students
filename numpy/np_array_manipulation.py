import numpy as np

# create numpy 2D array
lst = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])

#indexing on np arrays is similar to indexing of lists
#lst[m][n] gives nth element in mth row
element = lst[1][0] 

np.min(lst) #gives min of lst
np.max(lst) #gives max of lst
np.average(lst) #gives average of lst
np.diagonal(lst) #gives the diagonal
np.size(lst) #gives numpy of elements in lst

#Extract all odd numbers from arr

arr = np.arange(10)
print(arr[arr % 2 == 1]) #Use of this func in numpy avoids the usage of for loop

#Replace all odd numbers in arr with -1
print(arr[arr%2 == 1] = -1)

#But the above method modifies the array arr

#Replace all odd numbers without changing arr
#This can be done using the function 'where'

out = np.where(arr % 2 == 1, -1, arr)
print(out) 

#Converting the 1D array to 2D array
arr.reshape(2, -1) #Setting to -1 automatically decides the number of cols

np.repeat(1, 10) #gives the array with element 1 repeated 10 times
b = np.repeat(1, 10).reshape(2, -1)



