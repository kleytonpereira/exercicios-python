numero = []

while True:
    try:
        entrada = int(input('Digite o numero:'))

        if entrada == 0:
            break
        
        numero.append(entrada)
        
    except ValueError:
        print('Entrada Invalida')

print(f'Resultado final: {sum(numero)}')