# python3 Basics/ds/arr_copy.py

from numpy import *

arr1 = array([1,2,3,4,5])
arr2  = arr1
arr2  = arr1.view()

print(id(arr1))
print(id(arr2))