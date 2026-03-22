num1 = int(input("Enter value num1 :"))
num2 = int(input("Enter value num2 :"))

op = input("Enter operation :")

match op:
    case "+":
        print(num1, "+", num2, "=", num1 + num2)
    case "-":
        print(num1, "-", num2, "=", num1 - num2)
    case "*":
        print(num1, "*", num2, "=", num1 * num2)
    case "/":
        print(num1, "/", num2, "=", num1 / num2)
    case _:
        print("Invalid operation")


# python3 Basics/loops/match_operation.py