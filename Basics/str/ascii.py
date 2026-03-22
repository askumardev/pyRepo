print([(chr(i), i) for i in range(65, 91)])
print("--------------------------------------------")
print([(chr(i), i) for i in range(97, 123)])
print("--------------------------------------------")
print("Dec  Char | Dec  Char | Dec  Char | Dec  Char")
print("-" * 50)

for i in range(32, 128, 4):  # printable ASCII starts at 32
    print(f"{i:3}  {chr(i):3} | "
          f"{i+1:3}  {chr(i+1):3} | "
          f"{i+2:3}  {chr(i+2):3} | "
          f"{i+3:3}  {chr(i+3):3}")
    print("-" * 50)
    

# python3 Basics/str/ascii.py