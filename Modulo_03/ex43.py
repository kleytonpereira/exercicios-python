lista_2 = []

for x in range(10):
    numero = int(input('Digite um numero: '))
    lista_2.append(numero)

    if x == 0:
        lista = [numero]
        continue
    elif numero >= lista[len(lista) - 1]:
        lista.append(numero)
        continue

    for y in range(len(lista)):
        if lista[y] < numero:
            continue
        
        lista.insert(y, numero)
        break

lista_2.sort()

print(f'Maior é: {lista[len(lista) -1]}, menor é: {lista[0]}, media é: {sum(lista) / len(lista)} e a lista ordenada é: {lista}')
print(f'Maior é: {lista_2[len(lista_2) -1]}, menor é: {lista_2[0]}, media é: {sum(lista_2) / len(lista_2)} e a lista_2 ordenada é: {lista_2}')

    

    
    
