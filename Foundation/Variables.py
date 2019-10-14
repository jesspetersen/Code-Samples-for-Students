# Local variables are variables that only work within a determined scope,
# e.g. variables defined inside a function.

def hello_local():
    a = "Hello world! I am a local called 'a'."
    print(a)

# If you try to access variable a outside the function scope, python will raise an error.
# Uncomment the line below and run the program to check the error.
# print(a)

# If you call the function hello, it will print 'a' without errors because 'a' is defined inside the function.
hello_local()


# Non-local variables are variables that can be accessed by nested functions defined within functions.
# You need to state that you will be using them as non-local variables when you change the scope.
def hello_non_local():
    b = "Hello world! I am a local variable called 'b'."
    print(b)
    def nested_function():
        nonlocal b
        b = "Hello world! Now I am a non-local variable called 'b'." # This updates the value of b.
    nested_function()
    print(b)

hello_non_local()

# Global variables are variables that are in the main body of your code and can be used inside functions
# and classes without explictly passing them as arguments or defining them within the function or
# class scope. But you need to state that you will be using them as global variables when you change
# the scope.
c = "Hello world! I am a global variable called 'c'."

def hello_global():
    global c
    print(c)

hello_global()
