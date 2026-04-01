def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print("=" * 30)
print("      Python Calculator")
print("=" * 30)
print("Operators: +  -  *  /")
print("Type 'exit' to quit")
print("=" * 30)

while True:
    try:
        user_input = input("\nEnter expression (e.g. 5 + 3): ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        for op in operations:
            if op in user_input:
                parts = user_input.split(op)
                if len(parts) == 2:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())
                    result = operations[op](a, b)
                    print(f"Result: {a} {op} {b} = {result}")
                    break
        else:
            print("Invalid input. Use format: number operator number (e.g. 5 + 3)")

    except ValueError:
        print("Invalid numbers. Please enter valid numeric values.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
    

# python3 projs/calculator.py