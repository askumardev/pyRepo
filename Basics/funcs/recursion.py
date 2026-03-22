# python3 Basics/recursion.py


def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

# 🔥 Example usage
num = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {num} is:", factorial(num))

print("---------------------------------")


def fib(n):
  if(n==0 or n==1):
    return n
  return fib(n-1) + fib(n-2)

num = int(input("Enter the Fibonacci index: "))
result = fib(num)
print(f"Fibonacci number of {num} is: {result}")

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