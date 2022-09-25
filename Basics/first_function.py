# python3 Basics/first_function.py

def fun():
	print("*****first function*****")

def add(a,b):
	c = a + b
	#print(c)
	return c

def add_sub(a,b):
	c = a + b
	d = a - b
	#print(c)
	return c,d

fun() #*****first function*****
print(fun()) #*****first function***** && None

res = add(5,4)
print(res)

res1,res2 = add_sub(15,4)
print(res1,res2)

#A function can execute instructions and return a value