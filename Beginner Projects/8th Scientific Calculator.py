print('''
 _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

''')

def calculator():
    def calculate(num1, operator, num2):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 != 0:   
                return num1 / num2
            else:
                return "Error! Division by zero."
        else:
            return "Invalid operator!"

    num1 = float(input("What's the first number?: "))
    while True:
        operator = input("Pick an operation (+, -, *, /): ")
        num2 = float(input("What's the next number?: "))
        result = calculate(num1, operator, num2)
        print(f"{num1} {operator} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = result
        else:
            num1 = float(input("What's the first number?: "))


calculator()
