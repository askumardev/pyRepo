password = "Y2K123"
pwd = input("Enter password :")

while pwd != password:
    print("Incorrect password, try again")
    pwd = input("Enter password :") 
print("Correct password, welcome!")