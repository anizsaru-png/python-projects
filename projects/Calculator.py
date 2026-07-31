def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero")
                continue
            result = num1 / num2
        else:
            print("Invalid operation")
            continue
        
        print(f"Result: {num1} {op} {num2} = {result}")
        
        again = input("Calculate again? (y/n): ")
        if again.lower() != 'y':
            break

calculator()