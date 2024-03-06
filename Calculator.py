# Tahj McClain
# This program will be basic calculator

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

while True:
#menu to decide what operation to perform
    print("Select operation.")
    selection = input('1: addition\n2: subtraction\n3: multiplication\n4: division\n5: to quit\n')
    while selection != '5':
        if selection in ('1', '2', '3', '4'):
            try:
                num1 = float(input('Enter first number: '))
                num2 = float(input('Enter second number: '))
            except ValueError:
                print('Invalid input. Enter a valid number ')
                continue
            if selection == '1':
                print(num1 + num2)
            elif selection == '2':
                print(num1 - num2)
            elif selection == '3':
                print(num1 * num2)
            elif selection == '4':
                print(num1 / num2)

        selection = input('1: addition\n2: subtraction\n3: multiplication\n4: division\n5: to quit\n')
    else:
        break








