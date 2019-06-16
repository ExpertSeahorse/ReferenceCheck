def square(num):
    return num ** 2


def even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# The "map()" func runs an entire list through a function (not written to a var); needs iteration to run correctly
a= list(map(square, my_nums))
print(a)

# "filter()" runs a list thru a boolean method and return all values evaluated to be true
b= list(filter(even, my_nums))
print(b)


'''
def square(num):
    return num ** 2

Is equal to:

lambda num: num**2

Use this for map/filter funcs
'''

"""
VARIABLE RULES
######################
L E G B
Local:      vars within function 
Enclosing:  vars within any outer functions
Global:     vars declared global or in first few lines of file
Built-in:   preassigned names (print, range, list, etc.)
"""