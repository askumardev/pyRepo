class Student:

    school = "vikas"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Getter
    def get_m1(self):
        return self.m1

    # Setter
    def set_m1(self, value):
        self.m1 = value

    # Class method (without decorator → use class directly)
    def get_school():
        return Student.school

    # Static-like method (just normal method)
    def info():
        print("Static method demo")


# Usage
s1 = Student(500, 34, 45)
print("------------below is the getter 500 -----------------------")
print(s1.get_m1())   # getter
print("------------below is the setter 200 -----------------------")
s1.set_m1(200)       # setter

print(s1.get_m1())

print(s1.avg())

print(Student.get_school())
Student.info()