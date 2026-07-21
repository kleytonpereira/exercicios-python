numero = int(input())

for x in range(numero):
    if x == 0:
        print('0')
        anterior = 0
        fibonnaci = 1
        continue

    print(f'{fibonnaci}')
    temp = anterior
    anterior = fibonnaci
    fibonnaci += temp