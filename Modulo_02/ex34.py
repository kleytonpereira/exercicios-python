numero = input()
numero_original = int(numero)

contrario = str()

for x in range (len(numero)):
    if x == 0:
        contrario = str(int(numero) % 10)
        continue

    temp = int(numero) // 10 ** x
    contrario += str(temp % 10)

numero_invertido = int(contrario)

if numero_original == numero_invertido:
    print('Sim')
else:
    print('Não')