def moda(*numeros):
    contagem = dict()

    for numero in numeros:
        if numero not in contagem:
            contagem[numero] = 1
        else:
            contagem[numero] += 1

    for y in contagem.items():
        if max(contagem.values()) == y[1]:
            maior = y
            break

    return(maior[0])

    


assert moda(1,4,5,3,4,4,6,7) == 4, 'Não passou'