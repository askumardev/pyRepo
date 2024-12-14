# python3 DSA/arr_matrices.py

from numpy import *

arr1 = array([
              [1,2,3,4],
              [4,5,6,7]
            ])

m1 = matrix('1 2 3 4 ; 4 5 6 7') #alt way of multi dimentional arr
m = matrix(arr1)
m2 = matrix('1 2 3 ; 4 5 6 ; 5 6 7')
m3 = matrix('1 2 4 ; 2 5 6 ; 7 6 8')

print(m)
print(m1)

print(m2)
print(diagonal(m2))
print(m2.min())
print(m2.max())

m4 = m2 * m3
print(m4) #matrix multiplcation