import math

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

def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def display_menu():
    print("\nExtended Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Square Root")
    print("8. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result is: {modulus(num1, num2)}")
            elif choice == '6':
                print(f"The result is: {exponentiation(num1, num2)}")
        elif choice == '7':
            num = float(input("Enter number to find square root: "))
            print(f"The result is: {square_root(num)}")
        elif choice == '8':
            print("Exiting Calculator Application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
