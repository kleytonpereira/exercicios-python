peso = float(input())
altura = float(input())

imc = peso / altura ** 2
    
match imc:
    case _ if 0.0 < imc < 18.5:
        print('Baixo peso')
    case _ if imc < 25:
        print('Peso Adequado')
    case _ if imc < 30:
        print('Sobrepeso')
    case _ if imc < 35:
        print('Obesidade I')
    case _ if imc < 40:
        print('Obesidade II')
    case _:
        print('Obesidade III')