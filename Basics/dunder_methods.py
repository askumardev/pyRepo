str1 = "hello"
str2 = "world"

# newStr = str1 + str2
newStr = str1.__add__(str2)
print(newStr)
print(str1.__len__())


def func():
    pass

print(type(func))