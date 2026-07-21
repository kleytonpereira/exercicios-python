def estatisticas(numeros):
    resultado = {'minimo': 0, 'maximo': 0, 'media': 0, 'mediana': 0}

    numeros.sort()

    resultado['minimo'] = numeros[0]
    resultado['maximo'] = numeros[len(numeros) - 1]

    resultado['media'] = sum(numeros) / len (numeros)
    
    if len(numeros) % 2 != 0:
        resultado['mediana'] = numeros[round(len(numeros) / 2)]
    else:
        resultado['mediana'] = (numeros[int(len(numeros) / 2)] + numeros[(int(len(numeros) / 2) + 1)]) / 2

    return resultado

assert estatisticas([10, 4, 3, 5, 3, 7, 41, 9]) == {'minimo': 3, 'maximo': 41, 'media': 10.25, 'mediana': 8}, 'Não passou'
