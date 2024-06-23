# python3 Basics/ds/arr_copy.py
# 3 types of copy mechanisms

from numpy import *

arr1 = array([1,2,3,4,5])
arr2  = arr1
arr2  = arr1.view() ##shallow copy
arr3  = arr1.copy() ##deep copy

arr1[1] = 7

print(id(arr1))
print(id(arr2))

print(arr1)
print(arr2) ##shallow copy
print(arr3)