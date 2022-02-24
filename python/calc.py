# honestly idk how this is lesson 1 but it might help

def eqInput(message):
    """creates input for float value, added message required"""
    inputted = float(input(message))
    return inputted


def operationSelect(operations):
    """creates dialouge for user to select operation from list of operations"""
    print("Operations:")
    for x in operations:
        print(x)
    operationSelected = str(input("Which operation?"))
    return operationSelected


def calculate(no1, no2, operation):
    """calculates with two inputs and an operation"""
    try:
        if operation == "+":
            return no1+no2
        elif operation == "-":
            return no1-no2
        elif operation == "*":
            return no1*no2
        elif operation == "/":
            return no1/no2
        elif operation == "**":
            return no1**no2
    except:
        return "error"


operationList = ["+", "-", "*", "/", "**"]

print("calculator")
num1 = eqInput("first number")
num2 = eqInput("second number")
operation = operationSelect(operationList)
print("answer:", calculate(num1, num2, operation))
