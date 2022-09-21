#Datatypes
#----------------------------------------
#None, Numeric, List,
#Tuple, Set, String, Range, Dictionary
#----------------------------------------
#Numeric - int,float,complex,bool
#-----------------------------------------------------------------------------
# Immutable data types --> int,long,float,complex,str,byte,stuple,frozenset
# Mutable data types --> bytearray,list,set,dict
#------------------------------------------------------------------------------

#String
str1 = "Hello, world..."
print(str1) #Hello, world...
print(type(str1)) #<class 'str'>

#Integer
x = 123
print(x) #123
print(type(x)) #<class 'int'>

#Float
pi = 3.14159
print(pi) #3.14159
print(type(pi)) #<class 'float'>

#complex
num = 6 + 9j
print(type(num)) #<class 'complex'>
print(num) #(6+9j)

#Boolean
boolx = True
print(boolx) #True
print(type(boolx)) #<class 'bool'>
booly = False
print(booly) #False
print(type(booly)) #<class 'bool'>

a = None
print(a) #None
print(type(a)) #<class 'NoneType'>

#type conversions
a = 5.6
b = int(a)
print(b) #5

c = float(b)
print(c) #5.0

s = "123.456"
#s1 = int(s) #ValueError: invalid literal for int() with base 10: '123.456'
s2 = float(s)
print(s2) #123.456
print(int(s2)) #123

# python3 pyConcepts/pyBasics/var_data_types.py