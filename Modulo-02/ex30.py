while True:
    entrada = input('Qual operação quer realizar: ')

    if entrada == '1-somar':
        numero_01 = int(input('Digite o primeiro numero: '))
        numero_02 = int(input('Digite o segundo numero: '))
        print(f'Resultado da soma: {numero_01 + numero_02}')
    elif entrada == '2-subtrair':
        numero_01 = int(input('Digite o primeiro numero: '))
        numero_02 = int(input('Digite o segundo numero: '))
        print(f'Resultado da subtratação: {numero_01 - numero_02}')
    elif entrada == '3-sair':
        break
    else:
        print('Entrada Invalida')