a = b = c = 2
print(a,b,c) #2 2 2

a,b,c = 1,2,3
print(a,b,c) #1 2 3

a,b,_ = 4,5,6
print(a,b,_) #4 5 6

# a,b,_ = 4,5,6,7
# print(a,b,_) #4 5 6 #ValueError: too many values to unpack (expected 3)

#a,b,c = 1,2
#print(a,b,c) #ValueError: not enough values to unpack (expected 3, got 2)

#a,b = 1,2,3
#print(a,b,c) #ValueError: too many values to unpack (expected 2)

# python3 Basics/var_declaration.py