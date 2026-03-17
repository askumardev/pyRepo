# python3 Basics/generator.py

def multiple_yield():
  str1 = "First String"
  yield str1

  str2 = "Second string"
  yield str2

  str3 = "Third String"
  yield str3

obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))