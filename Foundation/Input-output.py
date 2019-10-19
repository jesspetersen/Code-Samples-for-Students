'''
###Python Output using print() function###
We use the print() function to output data to the standard output device (screen).
'''

print('This sentence is output to the screen')
# Output: This sentence is output to the screen

a = 5

print('The value of a is', a)
# Output: The value of a is 5

'''
The actual syntax of the print() function is
*****************************************************************
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
*****************************************************************

Here, objects is the value(s) to be printed.

The sep separator is used between the values. It defaults into a space character.
After all values are printed, end is printed. It defaults into a new line.

The file is the object where the values are printed and its default value is sys.stdout (screen). 
Here are an example to illustrate this.
'''

print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&

'''
###Output formatting###
we can use str.format() to format the string output

Here the curly braces {} are used as placeholders. 
We can specify the order in which it is printed by using numbers (tuple index)
'''

print('the first one is {0} and the second one is {1}'.format('A','B'))
# Output: the first one is A and the second one is B

print('now, the first one is {1} and the second one is {0}'.format('A','B'))
# Output: the first one is B and the second one is A

'''
We can use keyword arguments to format the string.
'''

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
# Output: Hello John, Goodmorning

'''
We can format strings like the old sprintf() style used in C programming language. 
We use the % operator to accomplish this.
'''
x = 12.3456789
print('The value of x is %3.2f' %x)
# Output: The value of x is 12.35

print('The value of x is %3.4f' %x)
# Output: The value of x is 12.3457

'''
###Python Input###
to take the input from the user, we use input()
*****************************************************************
input([prompt])
*****************************************************************
where prompt is the string we wish to display on the screen. It is optional.
'''
num = input('Enter a number: ')
# Terminal: 
# >>> Enter a number: 10
# >>> num
# Output: '10'

'''
Here, we can see that the entered value 10 is a string, not a number. 
To convert this into a number we can use int() or float() functions.
'''

num = int(input('Enter a number: '))
# Terminal: 
# >>> Enter a number: 10
# >>> num
# Output: 10

'''
This same operation can be performed using the eval() function. 
But it takes it further. It can evaluate even expressions, provided the input is a string
'''

print(eval('2+3'))
# Output: 5
