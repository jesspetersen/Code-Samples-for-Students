# Errors in python are called exceptions and are handled through the use of try/except blocks

# Use a try statement when you think the program could raise an exception
try:
    age = input("Enter your age: ")
    # If the user didn't enter a number the program will through a 'ValueError' here
    age = int(age)
except ValueError:
    # The excpetion is caught and instead of crashing the program runs the code in this block
    print("You did not enter a number!")
except KeyboardInterrupt:
    # You can catch multiple types of exceptions in a single block
    print("You pressed CTRL+C")
except Exception as e:
    # You can use the type 'Exception' to catch all types of errors
    # You can also use the 'as' keyword to store the exception in a variable
    print("An error occured :(")
    print(f"Error type: {e}")
