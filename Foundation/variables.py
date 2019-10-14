# ----------------- VARIABLES -------------------- #

# Variables, in Python, and any other programming language, are pointers to a memory location that are used to store some data or value
# Put simply variables are used to store values during program execution
# In Python, variable are dynamically typed; meaning a certain variable can store any type of data over the course of the program execution
# Unlike, other languages, say Java, where you specify the type of data the is to be stored in the variable
# So, let's try an create our first Python variable

# In Python, a variable has a name/identifier, known as the variable name
# There are rules to followed when naming variable:

## Variables names must start with a letter or an underscore, such as:
### _underscore
### underscore_

## The remainder of your variable name may consist of letters, numbers and underscores.
### password1
### n00b
### un_der_scores

## Names are case sensitive.
### case_sensitive, CASE_SENSITIVE, and Case_Sensitive are each a different variable.

# Therefore, Python variables cannot start with any other character apart from a letter and underscore
# i.e. digits and other special characters cannot be used to start a Python variable name
# In addition, other special characters cannot be used within the variable name
# Thus, a Python variable can only include (A-Z), (a-z), (0-9) and _

first_python_variable = "" # this is an example of a valid Python variable name
second_python_variable = 0

# Apart from variable naming rules there are naming conventions popular among Python programmers

## Readability is very important. Which of the following is easiest to read? I’m hoping you’ll say the first example.
### python_puppet
### pythonpuppet
### pythonPuppet

## Descriptive names are very useful. If you are writing a program that adds up all of the bad puns made in this book, which do you think is the better variable name?
### total_bad_puns
### super_bad

## Avoid using the lowercase letter ‘l’, uppercase ‘O’, and uppercase ‘I’. Why? Because the l and the I look a lot like each other and the number 1. And O looks a lot like 0.

# Although Python is dynamically typed, you might however, be aware of the data you'll be working with

python_string_variable = "A Python string variable"
python_int_variable = 10
python_boolean_variable = True

# These variables will keep their values until they are explicitly changed
# As mentioned earlier, the variable can take any type of data, irregardless of its first data

python_string_variable = False
python_int_variable = "Just changed this int variable to a string variable"
python_boolean_variable = 1

# As you can see, the variable name comes first and is equated to its respective value, and not the other way

variable = "variable value"

# Something like:
0 = variable # is wrong. The Python interpreter will throw and error

# Variables can also be store values in other variables - variables can be equated to other variables
variable_1 = 1000
variable_2 = variable_1 # variable_2 === 1000

boolean_1 = False
boolean_2 = True

boolean_1 = boolean_2 # boolean_1 === True

# Other Python functions can be used with variables too
# Let's look at an example of printing a value is a variable

our_variable = "Hello, world!"

print(our_variable) # prints Hello, world!

# This is basically what variables are in Python
# It's a brief introduction
# More can be said about Python variables, really
# But I hope this helps nonetheless
# I'll also try and contribute to the other sections too. :)


# (c) 2019 Tafadzwa Muteke. All rights reserved.
# https://github.com/tmuteke