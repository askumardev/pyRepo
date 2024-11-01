# python3 Basics/add_digits.py
def add_digits(num):
    if len(str(num)) < 2:
        return num
    arr = [int(x) for x in str(num)]
    sum_digits = sum(arr)
    return add_digits(sum_digits)

print(add_digits(12))
print(add_digits(123))
print(add_digits(1234))
print(add_digits(8))