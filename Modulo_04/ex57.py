def eh_par(numero):
    return numero % 2 == 0

assert eh_par(2) == True, 'É par'
assert eh_par(3) == False, 'É impar'
assert eh_par(0) == True, 'Zero é par também'