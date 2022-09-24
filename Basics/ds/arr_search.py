# python3 Basics/ds/arr_search.py

from array import *

arr = array('i',[])
n = int(input("Enter length:: "))

for i in range(n):
  x = int(input("Enter next value:: "))
  arr.append(x)

print(arr)

k = 0
val = int(input("Enter a value to search:: "))
for e in arr:
  if e==val:
    print(k)
    break

  k+=1
print("*****************")
print(arr.index(val))
