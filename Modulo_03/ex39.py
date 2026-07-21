palavra = input('Digite a palavra: ')

y = len(palavra)

for x in range(len(palavra)):
    if x >= y:
        resultado = 'Sim'
        break
    elif palavra[x] == palavra[y-1]:
        y -= 1
    else:
        resultado = 'Não'
        break

print(resultado)