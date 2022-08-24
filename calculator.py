def greet():
    name = input("Please enter your name: ")
    print("Welcome to calculator " + name + "!")


def calculator():
    ans = 0
    print("What would you like to do?: ")
    print("Please enter'*' for multiplication, '/' for division and '%' to find modulo")
    print("Please enter '+' for addition, '-' for subtraction")
    operation = input("Please enter operation: ")

    first_number = int(input("Please enter your first number: "))
    second_number = int(input("Please enter your second number: "))

    def addition(num1, num2):
        return num1 + num2

    def subtraction(num1, num2):
        return num1 - num2

    def multiplication(num1, num2):
        return num1 * num2

    def division(num1, num2):
        if num2 == 0:
            print("invalid math operation, cannot divide by 0")
        else:
            return num1 / num2

    def modulo(num1, num2):
        return num1 % num2

    if operation == '+':
        ans = addition(first_number, second_number)

    elif operation == '-':
        ans = subtraction(first_number, second_number)

    elif operation == '*':
        ans = multiplication(first_number, second_number)

    elif operation == '/':
        ans = division(first_number, second_number)
    elif operation == '%':
        ans = modulo(first_number, second_number)
    else:
        print("Invalid Math operation")

    print(first_number, operation, second_number, "=", ans)
    calculate_again()


def calculate_again():
    answer = input("Do you want to perform another task? ")

    if answer == 'y' or answer == 'Y':
        calculator()
    else:
        print("See you soon!")


greet()
calculator()
