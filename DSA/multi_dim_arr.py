# python3 Basics/ds/multi_dim_arr.py

# below are the ways of creating arrays using numpy
# array,linspace,logspace,arange,zeros,ones

from array import *
from numpy import *

arr1 = array([1,3,5,7])
arr1a = array([1,3,5,7.5])
arr2 = array(([1,2,3],[4,5,6]))
arr3 = linspace(0,15)
arr4 = arange(0,15,2)
arr5 = logspace(1,40,5)
arr6 = zeros(5)
#arr7 = ones(5) 
arr7 = ones(5,int)

print(arr1) #[1 3 5 7]
print(arr1a) #[1.  3.  5.  7.5]
print(arr2) #[[1 2 3] [4 5 6]]
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)