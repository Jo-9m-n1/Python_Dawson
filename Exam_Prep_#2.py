'''What would be the output of the following code?'''

def operation():
    try:
        numbers = [10, 0, 'a']
        for i in range(len(numbers)):
            print(100 // numbers[i])
    except ZeroDivisionError:
        print("Division by zero error")
    except TypeError:
        print("Type error") 
    finally:
        print("Execution completed")

operation()