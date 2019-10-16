#!usr/bin/python3
#This serves to introduce functions to the students
#Functions are meant to reduce redundancy when writing code
#Hence, instead of writing the same code over and over, you can just call a function
#The function in this example will take a range of number and add them together then return the output
#In shrt, a function accepts input and gives output


def addition(a, b):
    '''use def to define a function '''
    
    #define a variable to store the total
    sum_all = 0
    
    #loop through the range of numbers
    for i in range(a, b):
        sum_all += i
        
    #use te return method to produce output
    return sum_all

#Calling the function
#Assign the function to a variable and provide parameters
result = addition(0, 5)
print("The total is: {0}".format(result))
        
