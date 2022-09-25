# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

def add(a):
  return a + 10

result = add(5)
print(result)

print("****************")

x = lambda a : a + 10
y = lambda a : a * 10
sq = lambda a : a * a
print(x(5)) #15
print(y(5)) #50
print(sq(5)) #50

# python3 Basics/lambda.py 