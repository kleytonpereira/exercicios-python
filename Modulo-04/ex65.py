def saudacao(nome, hora=12):
    if hora < 12:
        return 'Bom dia ' + nome
    elif hora < 16:
        return 'Boa tarde ' + nome
    else:
        return 'Boa noite ' + nome

assert saudacao("Ana") ==  'Boa tarde Ana', 'Passou corretamente'
assert saudacao("Ana", 20) == 'Boa noite Ana', 'Passou corretamente'