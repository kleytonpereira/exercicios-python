entrada = input()

for x in range (len(entrada)):
    if x == 0:
        soma = int(entrada) % 10
        continue

    temp = int(entrada) // 10 ** x
    soma += temp % 10

print(soma)