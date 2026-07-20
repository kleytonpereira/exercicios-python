def celsius_p_f(c):
    print (c * 1.8 + 32)
    return round(c * 1.8 + 32)

def f_p_celsius(f):
    print ((f - 32) * (5 / 9))
    return round((f - 32) * (5 / 9))


assert 21 == int(f_p_celsius(celsius_p_f(21))), 'Conversão correta'