def sum(a, b): #a, b are parameters of the function sum
    '''Sum of two numbers a and b.
    param a: first number
    param b: second number
    return: sum of a and b
    '''
    c = a + b
    return c

print(sum.__doc__) # this will print the docstring of the function sum
print(sum(5, 10)) #5, 10 are arguments
# this will print the sum of 5 and 10
help(sum) # this will also print the docstring of the function sum