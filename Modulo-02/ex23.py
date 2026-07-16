for numero in range(1, 101):
    if numero % 3 != 0 and numero % 5 != 0:
        print(f'{numero}, ')
    elif numero % 3 == 0 and numero % 5 == 0:
        print('FizzBuzz, ')
    elif numero % 3 == 0:
        print('Fizz, ')
    else:
        print('Buzz, ')