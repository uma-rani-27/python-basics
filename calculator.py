def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, ^): ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "^":
        result = a ** b
    else:
        print("Invalid operation")
        return

    print("Result:", result)

calculator()
