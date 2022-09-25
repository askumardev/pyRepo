# python3 Basics/ds/multi_dimen_arr.py


from numpy import *

arr1 = array([
              [1,2,3,4,5,6],
              [4,5,6,7,8,9]
            ])
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()
print(arr2)

arr3 = arr2.reshape(3,4)
print(arr3)
arr3 = arr2.reshape(2,2,3)
print(arr3)