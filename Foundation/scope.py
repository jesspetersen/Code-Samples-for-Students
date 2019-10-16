# SCOPE

# We will look at scope in Python pertaining to variables
# Thus, global and local scope of Python variables

# In simple terms, the scope of a variable refers to the accessible of a variable in particular places in code

# With scope, there are two levels of variable scope
# Global scope and local scope

# Global Scope
# This refers to the top level scope of a variable
# A variable whose scope is global can be accessed virtually anyone within the code

global_scope_var = "My scope is global"


def access_global_var():
    # this function can see the global variable
    print(global_scope_var)  # Prints 'My scope is global'

# Therefore, if the value of the global variable is changed anywhere, all other parts of the code will use the new value henceforth


def change_global_var_value():
    # change value of global variable
    global_scope_var = "I have a new value"


print(global_scope_var)  # prints 'I have a new value'

# Local scope
# This refers to variables that are defined inside a particular function or class
# These variables are therefore, cannot be accessed globally or elsewhere except from within the functions or classes

# Let's create a local variable in a new function


def local_var_func():
    # this variable is local to this function and cannot be accessed elsewhere
    local_scope_var = "My scope is local"
    print(local_scope_var)  # prints 'My scope is local'


print(local_scope_var)  # NameError: 'local_scope_var' is not defined

# Therefore, local_scope_var is said to be local to local_var_func() function
# Similarily, global_scope_var is said to global, to the whole script, even in local_var_func() function
# Hence, global_scope_var has global scope and local_scope_var has local scope

# Again, I really hope you'll find this useful
# Please, do not hesitate to reach out for any queries or recommendations

# (c) 2019 Tafadzwa Muteke. All rights reserved.
# https://github.com/tmuteke
