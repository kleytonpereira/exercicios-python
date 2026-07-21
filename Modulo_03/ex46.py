nomes = ['Kleyton', 'Milena', 'Jeff', 'Lary', 'João', 'Joana', 'Maria']

inicial = input('Digite a inicial de um nome para encontrar aqui: ')
resultado= []

for x in nomes:
    if x[0].upper() != inicial.upper():
        continue
    resultado.append(x)

print(resultado)

    