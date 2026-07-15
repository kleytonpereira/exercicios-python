x = float(input())

y = x % 400
print(y)

y = x % 4
print(y)

y = x % 100
print(y)

if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
    print('Sim')
else:
    print('Não')