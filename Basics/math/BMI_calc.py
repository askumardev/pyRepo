# python3 Basics/math/BMI_calc.py

ht = float(input("Enter ur height in m: \n"))
wt = float(input("Enter ur weight in kg: \n"))

# bmi = wt / ht ** 2
# print(bmi) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

bmi = round(wt / ht ** 2)
if bmi < 18.5:
  print(f"Your  bmi is {bmi}, underweight")
elif bmi < 25:
  print(f"Your  bmi is {bmi}, normalweight")
elif bmi < 30:
  print(f"Your  bmi is {bmi}, overweight")
elif bmi < 35:
  print(f"Your  bmi is {bmi}, obese")
else:
  print(f"Your  bmi is {bmi}, clinically obese")
