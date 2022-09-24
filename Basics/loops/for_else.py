# python3 Basics/loops/for_else.py

nums = [12,15,18,20,22,26]

for num in nums:
  if num % 7 == 0:
    print(num)
    break
  # else:
  #   print("not found")
else:
  print("not found")