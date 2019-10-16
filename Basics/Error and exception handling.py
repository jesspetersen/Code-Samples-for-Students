# The basic idea of this algorithm is to help the understanding of the Python
# error and general exception handling.

# Python can be used as an advanced mathematical calculator.
# The 4 mathematical functions (the sum, subtraction, multiplication and division) are
# represented by the following operators.
#
# Operator          Operation
# addition              +
# subtraction           -
# multiplication        *
# division	            /

# Imagine that you created your algorithm to always take the first entry and add /
# subtract / multiply / divide by the second. When making it available to the user,
# he can either enter a letter (which gives the error in all math functions) or he puts
# the second entry equal to 0 (This will give error at the time of division).
# So that your algorithm doesn't break, let's do the treatment using try / cath

# The try block lets you test a block of code for errors.
try:
    # creation and initialization of variable
    # The user who passes variable values through the command prompt
    variable_1 = input("Enter the first integer value ")
    variable_2 = input("Enter the second integer value ")

    # make some spaces
    print("")
    print("")
    print("Results")

    # Sum variables
    result = int(variable_1) + int(variable_2)
    print("Addition %s and %s is: %s" % (variable_1, variable_2, result))

    # Subtraction
    result = int(variable_1) - int(variable_2)
    print("Subtraction %s and %s is: %s" % (variable_1, variable_2, result))

    # Multiplication
    result = int(variable_1) * int(variable_2)
    print("Subtraction %s and %s is: %s" % (variable_1, variable_2, result))

    # Division
    result = int(variable_1) / int(variable_2)
    print("Subtraction %s and %s is: %s" % (variable_1, variable_2, int(result)))

#The except block lets you handle the error.
except:
    print("Error: Something went wrong")