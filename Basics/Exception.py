# python3 Basics/Exception.py

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
  division = a / b
  print(division)
except:
  print("Please enter valid values.")


index = int(input("Enter the index: "))

try:
  my_list = [1, 2, 3, 4]
  print(my_list[index])
except IndexError: # specify the type
  print("Please enter a valid index.")

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# try:
#   division = a / b
#   print(division)
# except ZeroDivisionError: # specify the type
#   print("Please enter valid values.")