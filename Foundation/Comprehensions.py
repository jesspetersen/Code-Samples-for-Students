"""
Python provides a very elegant syntax for operating on different types of iterable objects, know collectively as
comprehensions. Below we will look through List, Set, and Dictionary Comprehensions.
"""

# List Comprehensions

# The first type of comprehensions that developers generally use are List Comprehensions. This is provides a compact
# syntax for creating a list by operating over some other iterator. To demonstate, let's look at a very simple example.
# Say that we have the following list of integers:

example_list = [1, 2, 3, 4, 5]

# Now imagine that we want another list that has all of the values of example_list multiplied by 2. Without list
# comprehensions, we could need to do something like this:

no_comp_list = []

for num in example_list:
    no_comp_list.append(num*2)

print(no_comp_list)

# This takes us three lines of code including a for loop. List comprehensions allow us to do this all in one line, and
# would look like this:

comp_list = [num*2 for num in example_list]

print(comp_list)

# As you can see, we are able to define our iteration over all of the elements example list and perform our
# multiplication in a single line.

# Comprehensions also provide us with the ability to do some very powerful add-hoc conditional filtering of our results.
# If we take our original list, but change the problem to say that our output list should be all of the members of
# example_list whose value multiplied by 2 is less than or equal to 6, we could write the following line of code.

conditional_list = [num*2 for num in example_list if num*2 <= 6]

print(conditional_list)

# Set Comprehensions

# While we covered most of what comprehensions in Python can do in previous section, it is good to know that this idea
# is applicable to more than just lists. Next, we will look at an example of how we can use a set comprehension. For
# this example, we will be looking at the values of the following dictionary:

example_dict = {"Mark": "Detroit",
                "Kerry": "New York",
                "Tim": "LA",
                "Stacey": "New York"}

# Let's assume that this dictionary holds key, value pairs of a person's name and their favorite city. Let's say that we
# want to have a set that tells us the unique values that were given for the city names in the dictionary (a set is
# perfect for this because it automatically removes duplicate values). Using a set comprehension, we could simply write
# the following:

unique_cities = {city for city in example_dict.values()}

print(unique_cities)

# Dictionary Comprehensions

# Finally, we will show an exaple of a dictionary comprehension. Since data lookup in a dictionary is extremely fast,
# it can be a great idea to build them when we know that we are going to need a fast reference for something later on.
# In this example we are going to do something trivial just to show how the list comprehension would work. Let's say
# that we have the two lists below:

list_1 = ["Hello", "Blue", "Chicken"]
list_2 = ["Hola", "Azule", "Pollo"]

# Now if we wanted to have a dictionary that maps the english words to their Spanish equivalents, we could create that
# through the following comprehension:

translation_dict = {list_1[i]: list_2[i] for i in range(len(list_1))}

print(translation_dict)