for x in range(10):
    numero = int(input('Digite um numero: '))

    if x == 0:
        lista = [numero]
    elif numero >= lista[len(lista) - 1]:
        lista.append(numero)
        continue

    for y in range(len(lista)):
        if lista[y] < numero:
            continue
        
        lista.insert(y, numero)
        break

print(f'Maior é: {lista[len(lista) -1]}, menor é: {lista[0]}, media é: {sum(lista) / len(lista)} e a lista ordenada é: {lista}')

    

    
    
