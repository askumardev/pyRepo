# python3 DSA/arr_append.py

from array import *

arr = array('i',[])
n = int(input("Enter length:: "))

for i in range(n):
  x = int(input("Enter next value:: "))
  arr.append(x)

print(arr)
