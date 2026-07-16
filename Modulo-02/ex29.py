numero = int(input())

cont = 0

while True:
    cont += 1
    numero //= 10

    if numero == 0:
        break

print(cont)