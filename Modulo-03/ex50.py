frase = input('Digite a frase: ')

frase = frase.split()
resultado = dict()

for x in frase:
    resultado[x] = len(x)

print(resultado)