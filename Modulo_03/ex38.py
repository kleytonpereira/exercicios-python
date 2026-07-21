frase = input('Digite a frase: ')
vogais = ['a', 'e', 'i', 'o', 'u']

cont = sum(frase.count(v) for v in vogais)

print(cont)