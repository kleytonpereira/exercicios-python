lado_a = float(input())
lado_b = float(input())
lado_c = float(input())


if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    if lado_a == lado_b and lado_a == lado_c:
        print('Triangulo Equiláteo')
    elif lado_a == lado_b or lado_a == lado_c:
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
else:
    print('Não é um triangulo')