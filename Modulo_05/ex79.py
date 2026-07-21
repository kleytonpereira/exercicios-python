numero_01 = input('Digite o primeiro numero que vai ser divido: ')
numero_02 = input('Digite o segundo numero que vai dividir: ')

try:
    resultado = float(numero_01) / float(numero_02)
except ZeroDivisionError:
    print('Não e possivel realizar divisão por zero')
except ValueError:
    print('Digita um numero valido, não é possivel converte caracteres em digitos')
except:
    print('Erro inesperado, comunique o suporte')
else:
    print(resultado)
finally:
    print('Foi realizado a tentativa de divisão')