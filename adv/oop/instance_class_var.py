# python3 adv/oop/instance_class_var.py

class Car:
  wheels = 4 #class variable

  def __init__(self):
    self.milage = 10 #instance variable
    self.company = "BMW" #instance variable

c1 = Car()
c2 = Car()

c1.milage = 8

print(c1.company, c1.milage, c1.wheels)
print(c2.company, c2.milage, c2.wheels)