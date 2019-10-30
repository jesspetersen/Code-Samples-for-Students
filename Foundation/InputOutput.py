# In python basic input and output is extremely simple

# To print something to the screen all you need to do is call the print function
print("I am printing something")
print("Here is something else")
# You can pass multiple paramters which are seperated with the sep parameter
# This defaults to a single space ' '
print("1", "2", "3", "4", "5", sep=",")
# You can use the end paramter to change what is added to the end of the string
# This defaults to a new line '\n'
print("HELLO", end='!\n')
print("Using many", end=' ')
print("prints but only", end=' ')
print("printing on a single line")

# Get input from the user is just as easy and done with the input function
name = input()
print(f"Your name is {name}")
# You can pass a string paramter to the input function so you have a prompt
age = input("Enter your age: ")
print(f"You are {age} years old")
