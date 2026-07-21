def inverte(texto):
    return texto[:: -1]

def eh_palindromo(texto):
    return texto.replace(' ', '') == inverte(texto).replace(' ', '')

assert eh_palindromo("a base do teto desaba") == True, 'É palindromo'
