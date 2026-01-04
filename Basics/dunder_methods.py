str1 = "hello"
str2 = "world"

# newStr = str1 + str2
newStr = str1.__add__(str2)
print(newStr)
print(str1.__len__())

# __str__() , __add__(), __sub__(), __mul__(), __repr__(), __init__()
# __truediv__(), __eq__(), __lt__(), __gt__(), __gte__(), __ne__()
# __getitem__(), __setitem__(), __delitem__(), __contains__(), __append__()

def func():
    pass

print(type(func))