# python3 numpy/array_demo.py

import numpy as np
arr = np.array('A')
print(arr.ndim)

arr1 = np.array([['A','B','C'], ['D','E','F']])
print(arr1.ndim)

# arr2 = np.array([[['A','B','C'], ['D','E','F']],
#                  [['G','H','I'], ['J','K']]])
# print(arr2.ndim)
# ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 2 dimensions. The detected shape was (2, 2) + inhomogeneous part.

arr2 = np.array([[['A','B','C'], ['D','E','F']],
                 [['G','H','I'], ['J','K','L']]])
print(arr2.ndim)
print(arr2.shape)
print(arr2[0][0][1])

arr3 = np.array([[['A','B','C'], ['D','E','F']],
                 [['G','H','I'], ['J','K',' ']]])
print(arr3.ndim)
word = arr3[0][0][0] + arr3[1][0][0]
print(word)