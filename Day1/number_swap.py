a = input("a:")
b = input("b:")
# swap logic
tmp = a
a = b
b = tmp

print("*************After swapping")
print("a="+ a)
print("b="+ b)

#==============Alt way============
c = 5
d = 6

c = c + d
d = c - d
c = c - d

print(c)
print(d)