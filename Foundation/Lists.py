#A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
fruit_list = ["apple", "banana", "cherry"]
print(f'This is my list: {fruit_list}\n')

#You can access the list items by referring the index number.
print(f'This is the second item of the list: {fruit_list[1]}\n')

#You can use negative indexing
#Negative indexing means beginning from the end. -1 refers to the last item, -2 refers to the second last item etc.
print(f'This is the last item of the list: {fruit_list[-1]}\n')

#You can adds elements at the end of the list with the method "append".
fruit_list.append('orange')
print(f'Now I have orange in my list: {fruit_list}\n')

#You can specify a range of indexes by specifying where to start and where to end the range.
print(f'These are the second and third list items: {fruit_list[1:3]}\n')

#To change the value of a specific item, you can refer to the index number and set a new value.
fruit_list[0] = 'melon'
print(f'Apple was replaced by Melon: {fruit_list}\n')

#You can check if the item is present in the list.
if 'orange' in fruit_list:
    print('Yes! Orange is on the list.\n')

# You can remove an item from the list by its value.
fruit_list.remove("melon")
print(f'Now the list has no melon: {fruit_list}\n')

# You can remove an item from the list by its index.
fruit_list.pop(0)
print(f'Banana item has now been removed: {fruit_list}\n')

# You can also remove an item from the list by its index using the del method.
del fruit_list[1]
print(f'Now the item orange has been removed: {fruit_list}\n')

#The split() method splits a string into a list.
meat_list ="pork,bacon,ham,hot dogs".split(',')
print(f'This is a new list: {meat_list}\n')

#you can join two list.
food_list = fruit_list + meat_list
print(f'This is the union of the list: {food_list}\n')

# You can also add one list to another
#Lists can have duplicate values
salad_list = ['carrots', 'broccoli', 'spinach', 'carrots']
food_list.extend(salad_list)
print(f'This is the union of the lists: {food_list}\n')

#Você tambem pode ordenar uma lista
food_list.sort()
print(f'Now the list is sorted in ascending order: {food_list}\n')
food_list.reverse()
print(f'Now the list is sorted in descending order: {food_list}\n')


