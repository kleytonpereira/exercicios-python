frase = input('Digite uma palavra/frase: ')
invertida = ''


for x in range(len(frase)-1, -1, -1):
    invertida += frase[x]

invertida_ = frase[::-1]

print(invertida)
print(f'Outra: {invertida_}')
