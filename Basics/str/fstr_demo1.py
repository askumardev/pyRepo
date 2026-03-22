template = "Dear {}, Take this {}$ gift"
name = input("Enter the name: ")
amount = input("Enter the amount: ")
message = template.format(name, amount)
print(message)


print(f"Dear {name}, Take this {amount}$ gift...")
# python3 Basics/str/fstr_demo1.py