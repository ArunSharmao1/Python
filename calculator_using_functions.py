# Function to perform addition
def addition(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtraction(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiplication(num1, num2):
    return num1 * num2

# Function to perform division
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    else:
        return num1 / num2

# Main function to handle user input and display results
def calculator():
    print("Welcome to Simple Calculator!\n")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)\n")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        result = addition(num1, num2)
        operation = "+"
    elif choice == '2':
        result = subtraction(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiplication(num1, num2)
        operation = "*"
    elif choice == '4':
        result = division(num1, num2)
        if isinstance(result, str):
            print(result)
            return
        else:
            operation = "/"
    else:
        print("Invalid choice!")
        return
    
    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Call the main function to start the calculator
calculator()
