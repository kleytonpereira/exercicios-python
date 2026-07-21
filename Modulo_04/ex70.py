def valida_senha(senha):
    contagem = {'minus': 0, 'maisc': 0, 'digito': 0, 'outro': 0}
    resultado = True

    if len(senha) < 8:
        print('Senha muito pequena, refaça')

    for letra in senha:
        if 91 > ord(letra) > 64:
            contagem['maisc'] += 1
        elif  123 > ord(letra) > 96:
            contagem['minus'] += 1
        elif letra.isdigit():
            contagem['digito'] += 1
        else:
            contagem['outro'] += 1
    
    if contagem['maisc'] == 0:
        print('Falta uma letra maiscula')
        resultado = False
    
    if contagem['minus'] == 0:
        print ('Falta uma letra minuscula')
        resultado = False

    if contagem['digito'] == 0:
        print('Falta um digito')
        resultado = False

    return resultado


assert valida_senha('@Kleyton10'), 'Não passou, senha fraca'
assert valida_senha('kleyton10') == False, 'Não passou, deveria indicar senha fraca'
assert valida_senha('Kleytooon') == False, 'Não passou, deveria indicar senha fraca'