produtos = ['banana', 'tomate', 'cebola', 'ovos', 'carne']
precos = [2, 5, 4, 15, 50]

resultado = dict()

resultado = {produto: preco for produto, preco in zip(produtos, precos)}

print(resultado)