import math
import mymodule
import os
import requests
# Using built-in functions
num = 16

print("Square root:", math.sqrt(num))
print("Power:", math.pow(2, 3))
print("Pi value:", math.pi)

print("---------------------------------")
# Using user-defined function from mymodule
mymodule.hello()

r = requests.get('https://www.example.com')
print(r.text)