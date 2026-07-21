def fatorial(numero):
    for fatorial in range (numero-1, 0, -1):
        numero *= fatorial
    return numero

def fatorial_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fatorial_rec(n - 1) * n


assert fatorial(5) == 120, 'Calculado correto'
assert fatorial_rec(5) == 120, 'Calculado correto'