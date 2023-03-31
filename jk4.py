def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    return num1, num2, op

def displayResult():
    num1, num2, op = takeInput()
    result = 0
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    print("{0} {1} {2} = {3}".format(num1, op, num2, result))

displayResult()
