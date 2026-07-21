valores = [41, 75, 74, 32, 66, 31, 51, 96, 97, 64, 55, 17, 80, 92, 
           38, 45, 12, 85, 4, 88, 46, 46, 53, 24, 53, 7, 62, 93, 0, 27]

resultado = {'maior': 0, 'segundo_maior': 0}

for valor in valores:
    if valor > resultado['maior']:
        temp = resultado['maior']
        resultado['maior'] = valor
        resultado['segundo_maior'] = temp

print(resultado)