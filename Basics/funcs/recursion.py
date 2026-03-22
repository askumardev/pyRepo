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
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


num = int(input("Enter the number of terms: "))

total = 0

print("Fibonacci Series:")

for i in range(num):
    value = fib(i)
    print(value, end=" ")
    total += value

print("\nSum of series:", total)

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