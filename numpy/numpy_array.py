#NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays.

#It is not the default package in python3, it has to be seperately installed.

#This program gives the syntax of creation of different types of arrays using numpy

#importing numpy package by aliasing
import numpy as np

#know the np version number
print(np.__version__)

#create a 1D numpy array
arr = np.arange(10)  #arange function is simliar to range function in python3
print(arr)

print(type(arr)) #gives <class 'numpy.ndarray'>


print(arr.shape) #we can use '.shape' attribute of numpy arrays to check the shape (dimension) of the array object

arr.dtype # dtype('int64') -> gives the data type of element stored in the array

lst = [1, 2, 3, 'j']
print(np.array(lst)) #create a numpy array using python3 list

#create a boolean array
b = np.ones((3, 3), dtype = bool) #creates a 3x3 numpy array of all True's
print(b)


#.reshape(m, n) function reshapes the array to m rows and n columns
arr.reshape(10, 1)


