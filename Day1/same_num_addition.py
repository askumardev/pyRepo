num = input("Enter a 2 digit number?\n")
print(type(num)) #<class 'str'>

first = num[0]
last = num[1]

result = int(first) + int(last)
print(result)