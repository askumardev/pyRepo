# python3 Basics/oop/multilevel_inheritance.py

class A:

  def m1(self):
    print("method1")
  
  def m2(self):
    print("method2")

a = A()
print("***A class methods***")
a.m1()
a.m2()

class B():

  def m3(self):
    print("method3")
  
print("***B class methods***")
b = B()
b.m3()

class C(A,B):
  def m4(self):
    print("method4")

print("***C class methods***")
c = C()
c.m1()
c.m2()
c.m3()
c.m4()
