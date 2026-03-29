class Person:
    def __init__(self, name, age):
        # constructor
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating objects
p1 = Person("Satish", 30)
p2 = Person("Kumar", 28)

# Calling method
p1.display()
p2.display()