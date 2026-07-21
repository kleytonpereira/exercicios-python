def maior_tres(a, b, c):
    if c <= a >= b:
        print(a)
        return a
    elif c <= b >= a:
        print(b)
        return b
    else:
        print(c)
        return c
    
assert 9 == maior_tres(9, 8, 7), 'Correto'
assert 10 == maior_tres(7, 10, 8), 'Correto'
assert 20 == maior_tres(8, 15, 20), 'Correto'
assert 8 == maior_tres(8, 8, 8),  'Correto'