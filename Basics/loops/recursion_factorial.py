# python3 Basics/recursion_factorial.py


def fact(n):
  if(n==0):
    return 1
  return n * fact(n-1)

result = fact(5)
print(result)





#import sys
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(2000)

# i=0
# def greet():
#   global i
#   i+=1
#   print("hello",i)
#   greet()

# greet() #RecursionError: maximum recursion depth exceeded while calling a Python object