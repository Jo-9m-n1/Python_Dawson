print('You are to enter two numbers, which I will divide for you')
print('Enter \'q\' to quit')

while True:
    first_number = input('Enter first number: ')
    if first_number == 'q':
        break

    second_number = input('Enter second number: ')
    if second_number == 'q':
        break
    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:   # When try block fails
        print('You cannot divide by zero!')
    else:   # When try block succeeds
        print(f'The result is {result}')

