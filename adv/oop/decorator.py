def greet():
    print("Hello")


def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper


# manually decorating
f = my_decorator(greet)

f()
print("---------using @decorator--------------------")

def my_decorator1(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator1 #decorator
def greet1():
    print("Hello...")

# # manually decorating
# greet = my_decorator(greet)

greet1()