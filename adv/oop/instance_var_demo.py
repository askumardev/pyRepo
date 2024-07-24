# python3 Basics/ObjCls/instance_var_demo.py

#instance variables differ for objects where as clas objects do not

class Employee:
  'Common base class for all employees'
  empCount = 0  #class variable

  def __init__(self, name, salary):
    self.name = name  #instance variable
    self.salary = salary #instance variable
    Employee.empCount += 1
   
  def displayCount(self):
    print( "Total Employee %d", Employee.empCount)

  def displayEmployee(self):
    print("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d", Employee.empCount)