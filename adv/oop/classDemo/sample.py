class Emp:
  company = "sample company"

  def sampleMethod():
    return "some text"
  
  def anotherMethod(self):
    return 34000

e = Emp()
# print(e.company)
print(Emp.sampleMethod())
print("-----------------------------")
e1 = Emp()
print(e1.anotherMethod())

# e1.sampleMethod() : Emp.sampleMethod() takes 0 positional arguments but 1 was given