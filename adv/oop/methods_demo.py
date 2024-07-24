# python3 Basics/ObjCls/methods_demo.py

class Student:

  school = "vikas"

  def __init__(self,m1,m2,m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3

  def avg(self):
    return (self.m1 + self.m2 + self.m3)/3

s1 = Student(23,34,45)
s2 = Student(34,45,67)

print(s1.avg())
print(s2.avg())