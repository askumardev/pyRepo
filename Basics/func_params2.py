## python3 Basics/func_params2.py
#  position,keyword,default, variable length arguments

def greet(str):
	print(str)

def sum(a,b):  #passing value by position
	c = a + b
	print("sum = ",c)

def person(name,age=45): ##passing value by default
  print(name)
  print(age)

def sum( a, *b ):  #variable length arguments
  "This prints a variable passed arguments"
  c = a

  for i in b:
    c = c + i
  print(c)

print("****passing value by position***")
greet("Hello")
sum(2,3)

print("****passing value by default***")
person(name="ramu") #passing by default

print("****passing value by keyword***")
person(age=34,name="ramu") #passing by keyword

print("****passin variable length arguments***")
sum( 10 )
sum( 20, 30, 40 )
