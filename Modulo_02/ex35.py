numero_01 = int(input())
numero_02 = int(input())

while True:
    if numero_01 == numero_02:
        resultado = numero_01
        break
    elif numero_01 > numero_02:
        temp = numero_01 % numero_02
    else:
        temp = numero_02 % numero_01

    numero_01 = numero_02
    numero_02 = temp

    if temp == 0:
        resultado = numero_01
        break

print(resultado)


        