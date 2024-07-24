# python3 Basics/ObjCls/innerCls.py

class Student:

  school = "vikas"

  def __init__(self,name,rollno):
    self.name = name
    self.rollno = rollno
    self.lap = self.Laptop()

  def show(self):
    print(self.name, self.rollno)

  class Laptop:
    def __init__(self):
      self.brand = "HP"
      self.ram = 8  


s1 = Student("satish",123)
s2 = Student("kumar",345)

s1.show()

print(s1.lap.brand)
lap1 = s1.lap
lap2 = s2.lap

print(lap1)
print(lap2)

l1 = Student.Laptop()

