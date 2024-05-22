def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    print("Simple Calculator")

    # Prompt user to enter the first number
    num1 = float(input("Enter the first number: "))

    # Prompt user to enter the second number
    num2 = float(input("Enter the second number: "))

    # Display operation choices
    print("Choose the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Prompt user to choose an operation
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Perform the chosen operation and display the result
    if choice == '1':
        result = add(num1, num2)
        operation = "addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "division"
    else:
        print("Invalid input")
        return

    print(f"The result of the {operation} is: {result}")


if __name__ == "__main__":
    calculator()
"# link" 
