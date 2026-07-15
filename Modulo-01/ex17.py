idade = int(input())

if idade > 17:
    print('Adulto')
elif idade > 14:
    print('Junior')
elif idade > 10:
    print('Infantil')
elif idade > 0:
    print('Mirim')
else:
    print('Entrada Invalida')