# python3 DSA/array.py

# Same as list but difference is all elements are of same type

# import array as arr
from array import *

arr1 = array('i',[5,6,7,8,9])
chars = array('u',['a','b','c'])
#arr2 = array('I',[5,6,7.5,8,9]) #TypeError: array item must be integer
arr3 = array('i',[5,-6,7,8,9])

print(arr1)
# val1 = arr1.reverse()
# print(val1)
print(arr1[1])
#print(arr2)
print(arr3)
print("*******************")
#for i in range(5):
for i in range(len(arr1)):
  print(arr1[i])
print("*******************")
for e in chars:
  print(e)
print("*******************")
newArr = array(arr1.typecode,(a*a for a in arr1))
for i in newArr:
  print(i)
print("*******while***********")
i = 0
while i < len(newArr):
  print(newArr[i])
  i+=1

