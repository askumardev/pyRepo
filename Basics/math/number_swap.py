# python3 Basics/math/number_swap.py

a = input("a:")
b = input("b:")
# swap logic
# tmp = a
# a = b
# b = tmp
a,b = b,a

print("*************After swapping")
print("a="+ a)
print("b="+ b)

#==============Alt way============
c,d = 5,6

c = c + d
d = c - d
c = c - d

print(c)
print(d)
#==============Alt way============
c,d = 5,6

c = c ^ d
d = c ^ d
c = c ^ d

print(c)
print(d)