# python3 Basics/Exception_alias.py

index = int(input("Enter the index: "))

try:
  my_list = [1, 2, 3, 4]
  print(my_list[index])
except IndexError as e:
  print("Exception raised:", e)


a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
  division = a / b
  print(division)
except ZeroDivisionError as err:
  print("Please enter valid values.", err)