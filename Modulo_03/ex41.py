palavra = input('Digite a palavra: ')

resultado = dict()

for x in palavra:
    if x not in resultado:
        resultado[x] = 1
    else:
        resultado[x] += 1

for y in resultado.items():
    if max(resultado.values()) == y[1]:
        maior = y
        break

print(maior)
print(resultado)