def calculator():

    try:
        first = int(input("Enter first number\n"))
        operator = input("Enter an operator\n")
        second = int(input("Enter second number\n"))
    except:
        return "Invalid input"

    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        return first / second
    else:
        return "invalid input"

print(calculator())
