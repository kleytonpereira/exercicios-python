import re

cpf = input('Digite o CPF: ')

resultado = re.match(r'\d\d\d\.\d\d\d\.\d\d\d-\d\d$', cpf)

if resultado:
    print('CPF valido')
    print(resultado)
else:
    print('CPF Invalido')