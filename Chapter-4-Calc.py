on = True

def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number ."))
    print(a+b)

def subtraction():
    a = float(input("Enter a number "))
    b = float(input("Enter another number "))
    print (a-b)

def multiply():
    a = float(input("Enter a number "))
    b = float(input("Enter another number "))
    print (a*b)

def divide():
    a = float(input("Enter a number "))
    b = float(input("Enter another number "))
    print (a/b)



while on:
    operation = input("Plesae choose +, -, *, / or q to quit ")
    if operation == '+':
        add()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':q
        on = False
        print("You quit the calculator")
    else:
        print("That operation is not availbe. ")

