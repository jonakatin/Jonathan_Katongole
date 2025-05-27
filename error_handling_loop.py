# Error handling with an infinite loop
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division:", result)
        break
    except ZeroDivisionError:
        print("Cannot divide by zero. Try again.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
