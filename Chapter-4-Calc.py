def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print (a + b)

 
def subtraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a * b)


def divide():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)

operation = input("Please choose +, -, * or / but means of typing one of the characters... ")
if operation == '+':
    add()
elif operation == '-':
    subtraction()
elif operation == '*':
    multiply()
elif operation == '/':
    divide()
else:
    print("You have chosen an invalid operation.")

