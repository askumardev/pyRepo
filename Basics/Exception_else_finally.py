# python3 Basics/Exception_else_finally.py

# We can add an else clause to this structure after except if we want to 
# choose what happens when no exceptions occur during the execution of the try clause

#  We can also add a finally clause if we need to run code that should always run, even if an exception is raised in try.

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
  division = a / b
  print(division)
except ZeroDivisionError as err:
  print("Please enter valid values.", err)
else:
  print("Both values were valid.")
finally:
  print("Finally!")