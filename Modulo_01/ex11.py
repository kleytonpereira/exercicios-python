numero_01 = float(input())
numero_02 = float(input())
operador = input()

match operador:
    case '+':
        print (numero_01 + numero_02)
    case '-':
        print (numero_01 - numero_02)
    case '*':
        print (numero_01 * numero_02)
    case '/':
        if numero_02 == 0:
            print('Impossivel dividir por zero')
        else:
            print(numero_01 / numero_02)
    case _:
        print('Operador invalido')