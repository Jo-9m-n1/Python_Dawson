flag = True
while flag:
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        result = number1 / number2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.\n")
    except ValueError:
        print("Error: Please enter an integer.\n")
    else:
        print(f"The result of dividing {number1} by {number2} is: {result}")
    flag = False