print("satish's laptop")  # satish's laptop
print('satish "kumar"')  # satish "kumar"
print('satish\'s "laptop"')  # satish's "laptop"

str = "abcdefgh"
# str[0] = 'X' #TypeError: 'str' object does not support item assignment
# MEANS STRINGS IN PYTHON ARE IMMUTABLE
# Slicing
print(str[3:])  # defgh
print(str[:5])  # abcde
print(str[2:5])  # cde
print(str[:])  # abcdefgh
print(str[::2])  # aceg

# Basic methods
name = "satishkumar"
print("si"+name[3:])  # siishkumar
print(len(name))  # 11

str1 = "Satish".lower()
print(str1)

str2 = str1.count("s")
print(str2)

print(str.upper())
str1 = "Hello World"
print(str1.split())  # ['Hello', 'World']
print(str1.split('e'))  # ['H', 'llo World']

# Use the dir() function to get all attributes and methods of the string object
string_methods = dir(str)
# Display the methods
# print(string_methods)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
# 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Display help for the count method
print(len(string_methods))  # 81

# python3 Basics/str/str_demo.py
