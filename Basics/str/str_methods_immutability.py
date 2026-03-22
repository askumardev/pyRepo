tst = "Python"
tst2 = "hello world"
tst3 = " Python is great"
text = "Apple,Banana,Cherry"
# tst[0] = "k"
# print(tst)  # TypeError: 'str' object does not support item assignment

print(tst.upper())  # PYTHON
print(tst.upper(), tst)  # PYTHON Python
print(len(tst))  # 6
print(tst.lower())  # python

print(tst2.title())  # Hello World
print(tst2.capitalize())  # Hello world
print(tst2.swapcase())  # HELLO WORLD

print(tst3.strip())  # Python is great
print(tst3.lstrip())  # Python is great
print(tst3.rstrip())  #  Python is great
print(tst3.find("is"))  # 8
print(tst3.replace("is", "was"))  #  Python was great

print(text.split(","))  # ['Apple', 'Banana', 'Cherry']
print(text.split(",")[0])  # Apple
print(text.split(",")[1])  #  Banana
print(text.replace(",", "|"))  # Apple|Banana|Cherry
print(text.replace(",", " | "))  # Apple | Banana | Cherry