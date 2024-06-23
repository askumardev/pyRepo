# python3 Basics/ds/arr_operations.py

from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,5])

print(concatenate([arr1,arr2])) #[1 2 3 4 5 6 7 8 9 5]

arr1 = arr1 + 5
print(arr1) #[ 6  7  8  9 10]

arr3 = arr1 + arr2
print(arr3) #[12 14 16 18 15]

print(sqrt(arr1))
print(sin(arr1))
print(cos(arr2))
print(log(arr3))

print(min(arr3)) #12
print(max(arr3)) #18