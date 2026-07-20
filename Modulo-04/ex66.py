def aplica(lista, funcao):
    return [funcao(x) for x in lista]

assert aplica([1,2,3,4,5], lambda n: n * 2) == [2, 4, 6, 8, 10], 'Não passou'