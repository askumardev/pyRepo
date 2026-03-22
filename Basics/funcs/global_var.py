def sum(a, b):
    global z #modifying global variable z inside the function
    z = 10 # this will change the value of z globally
    c = a + b + z
    return c

z = 20
result = sum(5, 10)
print("The sum is:", result)
print("The value of z is:", z) # this will print 10, not 20, because we modified z inside the function

# python3 Basics/funcs/global_var.py