resultado_01 = [x ** 2 for x in range(1, 21)]
resultado_02 = [x for x in range(1, 21) if x % 2 == 0]
resultado_03 = [(x, x**2) for x in range (1, 21)]

print(resultado_01)
print(resultado_02)
print(resultado_03)