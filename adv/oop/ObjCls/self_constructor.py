# python3 adv/oop/ObjCls/self_constructor.py

class Computer:

  def __init__(self):
    self.name = "satish"
    self.age = 23

  def update(self):
    self.age= 30

c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))

c1.name="kumar"
c1.age =12
c1.update()

print(c1.name)
print(c2.name)

print(c1.name)
print(c1.age)