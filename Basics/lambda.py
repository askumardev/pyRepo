# python3 Basics/lambda.py
# lambda using filter, map and reduce

# def isEven(n):
#   return n%2==0

# nums = [1,2,3,4,5,6,7,8,9]
# evens = list(filter(isEven,nums))
# print(evens)

from functools import reduce

nums = [1,2,3,4,5,6,7,8,9]

evens = list(filter(lambda n : n%2==0,nums))
plus2 = list(map(lambda n : n+2,evens))
double = list(map(lambda n : n*2,evens))
sum = reduce(lambda a,b : a+b,double)

print(evens)
print(plus2)
print(double)
print(sum)