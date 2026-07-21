import random

aleatorio = random.randint(0, 100)
cont = 0

while True:
    chute = int(input('De um chute que qual numero foi sorteado: '))
    cont += 1

    if chute == aleatorio:
        print('Parabens você acertou')
        break
    elif chute > aleatorio:
        print('O numero sorteado e menor')
    else:
        print('O numero sorteado e maior')

print(f'Numero de tentativa: {cont}')