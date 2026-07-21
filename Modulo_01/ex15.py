import random

aleatorio = random.randint(0, 10)

print('De um palpite de 0 à 10')

palpite = int(input())

if palpite == aleatorio:
    print('Acertou! Seu numero é igual ao sorteado')
else:
    print('Errou, o numero era:', aleatorio)
    print(f'Errou, o numero era: {aleatorio}')