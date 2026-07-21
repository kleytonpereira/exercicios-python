def conta_vogais(texto):
    return sum(texto.count(v) for v in ['a', 'e', 'i', 'o', 'u'])

assert conta_vogais('Banana') == 3, 'Banana tem 3 vogais'
assert conta_vogais('Maça') == 2, 'Maça tem duas vogais'