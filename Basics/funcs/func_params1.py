# python3 Basics/func_params1.py

# in python we dont have pass by value and pass by reference concepts

def update(x):
  print(id(x))

  x = 8
  print(id(x))
  print("x= ",x)

a = 10
print(id(a))
update(a)
print("a= ",a)
