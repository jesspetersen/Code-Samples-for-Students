# The basic idea of this algorithm is to help the understanding of the Python
# language arithmetic and logic operators.

# Python can be used as an advanced mathematical calculator.
# The 4 mathematical functions (the sum, subtraction, multiplication and division) are
# represented by the following operators.
#
# Operator          Operation
# addition              +
# subtraction           -
# multiplication        *
# division	            /

# creation and initialization of variable
# The user who passes variable values through the command prompt

variable_1 = input("Enter the first integer value ")
variable_2 = input("Enter the second integer value ")

#make some spaces
print("")
print("")
print("Results")

# Sum variables
result = int(variable_1) + int(variable_2)
print ("Addition %s and %s is: %s" %(variable_1, variable_2,result))

# Subtraction
result = int(variable_1) - int(variable_2)
print ("Subtraction %s and %s is: %s" %(variable_1,variable_2,result))

# Multiplication
result = int(variable_1) * int(variable_2)
print ("Subtraction %s and %s is: %s" %(variable_1,variable_2,result))

#Division
result = int(variable_1) / int(variable_2)
print ("Subtraction %s and %s is: %s" %(variable_1,variable_2,int(result)))