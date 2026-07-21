lista = [1, 2, 2, 3, 1, 4, 7, 6, 9]
resultado = []

for x in lista:
    if x not in resultado:
        resultado.append(x)

print(resultado)