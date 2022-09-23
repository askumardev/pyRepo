# python3 Basics/math/BMI_calculator.py

ht = input("Enter ur height in m: \n")
wt = input("Enter ur weight in kg: \n")

# bmi = wt / ht ** 2
# print(bmi) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

bmi = int(wt) / float(ht) ** 2
print(int(bmi))