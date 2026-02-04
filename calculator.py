# Developed by Md. Salauddin Sarker (https://salauddinsarker.com/)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: You cannot divide by zero!"
    return a / b

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b

history = []

while True:
    print("\n--- Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Power")
    print("7. Multiplication Table")
    print("8. View History")
    print("9. Quit")

    choice = input("Choose a number from 1 to 9: ")

    if choice == '9':
        print("See you next time!")
        break

    try:
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                print("Answer:", result)
                history.append(str(num1) + " + " + str(num2) + " = " + str(result))
            elif choice == '2':
                result = subtract(num1, num2)
                print("Answer:", result)
                history.append(str(num1) + " - " + str(num2) + " = " + str(result))
            elif choice == '3':
                result = multiply(num1, num2)
                print("Answer:", result)
                history.append(str(num1) + " * " + str(num2) + " = " + str(result))
            elif choice == '4':
                result = divide(num1, num2)
                print("Answer:", result)
                history.append(str(num1) + " / " + str(num2) + " = " + str(result))
            elif choice == '5':
                result = remainder(num1, num2)
                print("Answer:", result)
                history.append(str(num1) + " % " + str(num2) + " = " + str(result))
            elif choice == '6':
                result = power(num1, num2)
                print("Answer:", result)
                history.append(str(num1) + " ** " + str(num2) + " = " + str(result))
        elif choice == '7':
            num = float(input("Enter a number to see its table: "))
            for i in range(1, 11):
                print(num, "x", i, "=", num * i)
            history.append("Table for " + str(num))
        elif choice == '8':
            print("\n--- History ---")
            for item in history:
                print(item)
            if not history:
                print("No history found.")
        else:
            print("Oops! That choice is not on the list. Try again.")
    except ValueError:
        print("Invalid input! Please enter a numeric value for numbers.")





