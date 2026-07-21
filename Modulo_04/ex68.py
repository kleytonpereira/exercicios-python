import unicodedata

def normaliza(texto):
    resultado = ''
    for letra in texto:
        if  'WITH' in unicodedata.name(letra):
            divido = unicodedata.name(letra).split(' WITH')
            resultado += unicodedata.lookup(f'{divido[0]}')
        else:
            resultado += letra
            
    return resultado.lower()


assert normaliza('Ação') == 'acao', 'Não passou'