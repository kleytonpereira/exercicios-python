numero = int(input())

for linha in range(numero):
    print('')
    for coluna in range(numero):
        print('#', end='')

print('')

for linha in range(0, numero):
    print('')
    for coluna in range(numero - linha):
        print('#', end='')

print('')

for linha in range(0, numero):
    print('')
    for coluna in range(linha + 1):
        print('#', end='')

print('')