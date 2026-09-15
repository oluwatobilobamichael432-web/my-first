def calculator():

    num = input("Enter first number")
    operator = input("Enter an operator")
    ber = input("Enter second number")

    first = int(num)
    second = int(ber)


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
