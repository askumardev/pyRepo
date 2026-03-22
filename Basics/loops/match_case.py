a = int(input("Enter value a :"))
match a:
    case 1:
        print("Value is less than 10")
    case 3:
        print("Value is less than 30")
    case 6:
        print("Value is less than 60")
    case _:
        print("Value is not 1, 3, or 6")

# python3 Basics/loops/match_case.py