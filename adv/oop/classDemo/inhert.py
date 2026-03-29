class Animal:
    loc = "Hyderabad"  # class variable
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed

    def speak(self):  # method overriding
        print(f"{self.name} says Woof!")

    def show(self):
        print(f"Dog Name: {self.name}, Breed: {self.breed}")


class Cat(Animal):
    loc = "Bangalore"  # class variable
    def __init__(self, name, color):
        super().__init__(name)   # call parent constructor
        self.color = color

    def speak(self):  # method overriding
        print(f"{self.name} says Meow!")

    def show(self):
        print(f"Cat Name: {self.name}, Color: {self.color}")


# Main execution
d = Dog("Buddy", "Labrador")
c = Cat("Kitty", "White")

# Dog methods
d.show()
d.speak()
print(f"Dog Location: {d.loc}")  # Accessing class variable from Dog instance

print("-------------------")

# Cat methods
c.show()
c.speak()
print(c.loc)