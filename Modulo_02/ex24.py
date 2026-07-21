numero = int(input())

for fatorial in range (numero-1, 0, -1):
    numero *= fatorial
    print(fatorial)

print(numero)