tst = "Python"
tst2 = "hello world"
tst3 = " Python is great"
text = "Apple,Banana,Cherry"
text1 = "Python123"
# tst[0] = "k"
# print(tst)  # TypeError: 'str' object does not support item assignment

print(ord("P"))  # 80
print(chr(80))  # P

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
print(len(tst3))  # 19

print(text.split(","))  # ['Apple', 'Banana', 'Cherry']
print(text.split(",")[0])  # Apple
print(text.split(",")[1])  #  Banana
print(text.replace(",", "|"))  # Apple|Banana|Cherry
print(text.replace(",", " | "))  # Apple | Banana | Cherry

print(text1.isalnum())  # True
print(text1.isalpha())  # False
print(text1.isdigit())  # False
print(text1.islower())  # False
print(text1.isupper())  # False
print(text1.isnumeric())  # False
print(text1.isspace())  # False