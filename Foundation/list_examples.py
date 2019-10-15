#create a list
my_list = ['apples', 'bannanas', 'oranges']

#print list
print(my_list)

#print 2nd item in list, 1st item in list is indexed at 0
print(my_list[1])

#add item to list
my_list.append('peaches')

#delete item from list
my_list.remove('apples')

#change value of 1st item in list
my_list[0] = 'pears'

#loop through a list
for i in my_list:
    print(i)

#check if an item is in list
if 'oranges' in my_list:
    print('True')
else:
    print('False')

#print length of list
x = len(my_list)
print(x)

#empty list
my_list.clear()

#delete list
del my_list

#join 2 lists together
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']

list3 = list1 + list2
#or
for i in list2:
    list1.append(i)
