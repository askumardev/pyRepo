#Datatypes
#----------------------------------------
#None, Numeric, List,
#Tuple, Set, String, Range, Dictionary
#----------------------------------------
#Numeric - int,float,complex,bool
#----------------------------------------

#String
str1 = "Hello, world..."
print(str1[3])
print(type(str1))

#Integer
x = 123
print(x) #123
print(x + 7) #130
print(type(x)) #<class 'str'>
print(x) #123
x = x + 17
print(x) #140
#print(len(x)) #TypeError: object of type 'int' has no len()
str_x = str(x)
len_x = len(str_x)
print(len_x) #3
float_x = float(x)
print(float_x) #140.0
print("***************")
y = 1234567890000000000
print(y)
print(type(y)) #<class 'int'>

#Float
pi = 3.14159
print(pi)
print(type(pi)) #<class 'float'>
int_pi = int(pi)
print(int_pi)
#print(len(pi)) #TypeError: object of type 'float' has no len()

#complex
num = 6 + 9j
print(type(num)) #<class 'complex'>
print(num) #(6+9j)

#Boolean
bool = True
print(bool)
print(type(bool)) #<class 'bool'>
bool = False
print(bool)
print(type(bool)) #<class 'bool'>

#type conversions
a = 5.6
b = int(a)
print(b) #5

c = float(b)
print(c) #5.0