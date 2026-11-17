def calculator():
    memory = []
    while True:
        first_input = input("Enter first number\n")

        if first_input.lower() == "stop":
            break
        if first_input.lower() == "undo":
            if memory:
                removed = memory.pop()
                print("Removed:", removed)
            else:
                print("Nothing to undo")
            continue

        operator = input("Enter an operator\n")

        if operator.lower() == "stop":
            break

        if operator.lower() == "undo":
            if memory:
                removed = memory.pop()
                print("Removed:", removed)
            else:
                print("Nothing to undo")
            continue
        
        second_input = input("Enter first number\n")

        if second_input.lower() == "stop":
            break
        if second_input.lower() == "undo":
            if memory:
                removed = memory.pop()
                print("Removed:", removed)
            else:
                print("Nothing to undo")
            continue

        try:
            first = float(first_input)
            second = float(second_input)
        except:
            print("Invalid number")
            continue

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("Cannot divide by zero")
                continue
            result = first / second
        else:
            print("Invalid operator")
            continue

        memory.append(result)
        print(result)

calculator()
