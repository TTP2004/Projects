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
previous_answers = []
num3 = 0
while True:
#menu to decide what operation to perform
    print("Select operation.")
    selection = input('1: addition\n2: subtraction\n3: multiplication\n4: division\n5: display previous answers\n6: to quit\n')
    while selection != '6':
        if selection in ('1', '2', '3', '4'):
            try:
                num1 = float(input('Enter first number: '))
                num2 = float(input('Enter second number: '))
            except ValueError:
                print('Invalid input. Enter a valid number ')
                continue
            if selection == '1':
                num3 = num1 + num2
                previous_answers.append(num3)
                print(num3)
            elif selection == '2':
                num3 = num1 - num2
                previous_answers.append(num3)
                print(num3)
            elif selection == '3':
                num3 = num1 * num2
                previous_answers.append(num3)
                print(num3)
            elif selection == '4':
                num3 = num1 / num2
                previous_answers.append(num3)
                print(num3)
        selection = input('1: addition\n2: subtraction\n3: multiplication\n4: division\n5: display previous answers\n6: to quit\n')
        if selection == '5':
            print(previous_answers)
    else:
        break








