# python3 Basics/pdb_demo.py

import pdb 
 
def addition(a, b):
  answer = a + b
  return answer
 
 
pdb.set_trace()
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
sum = addition(x, y)
print("Sum of x and y is :",sum)