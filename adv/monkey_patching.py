# python3 adv/monkey_patching.py

class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print_user(self):
    print(f"The printed user name is: {self.name}")
    print(f"The printed user age is: {self.age}")

  def display_user(self):
    print(f"The displayed user name is: {self.name}")
    print(f"The displayed user age is: {self.age}")

u = User("John", 22)
u.print_user()
u = User("Cena", 25)
u.display_user()