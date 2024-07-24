# python3 Basics/oop/single_inheritance.py

class A:

  def m1(self):
    print("method1")
  
  def m2(self):
    print("method2")

a = A()
print("***A class methods***")
a.m1()
a.m2()

class B(A):

  def m3(self):
    print("method3")
  
  def m4(self):
    print("method4")
print("***B class methods***")
b = B()
b.m1()
b.m2()
b.m3()
b.m4()
