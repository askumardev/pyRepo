# python3 Basics/var/var_scope.py
# 
# #local vs global

a = 10 #Global
print(id(a))

def sayy():
  print("in sayy() a =",a)

def say():
  a = 15 #local
  #b = 8
  print("in say() a =",a)

def sayyy():
  global a
  a = 15 #local
  #b = 8
  print("in say() a =",a)

def global_ex():
  a = 9
  x = globals()['a']
  print(id(a))
  print("in func a =",a)

  globals()['a'] = 15

sayy()
say()
#global_ex()
#sayyy()


print("outside a =",a)
#print(b) #NameError: name 'b' is not defined