import math
from math import sin, radians
import mymodule
import os
import requests
# Using built-in functions
num = 16
b = sin(radians(90))
print("Square root:", math.sqrt(num))
print("Power:", math.pow(2, 3))
print("Pi value:", math.pi)
print("Sine of 90 degrees:", b)
print("---------------------------------")
# Using user-defined function from mymodule
mymodule.hello()

r = requests.get('https://www.example.com')
print(r.text)
print("---------------------------------")
r = requests.get('https://api.github.com')
print(r.json())