# python3 Basics/add_digits.py

def add_digits(num):
    if len(str(num)) < 2:
        return num
    if isinstance(num, str):
        arr = list(map(int, num.split()))
    else:
        arr = list(map(int, str(num)))
    sum_digits = sum(arr)
    return add_digits(sum_digits)

def sum_of_digits(num):
    if isinstance(num, str):
        num = int(num)
    if num == 0:
        return 0
    
    return (num % 10) + sum_of_digits(num // 10)

print(add_digits(12))
print(add_digits(123))
print(add_digits(1234))
print(add_digits(8))

print(add_digits("1234"))
print(add_digits("12"))
print("------------------")
print(sum_of_digits(9876))
print(sum_of_digits("9876"))