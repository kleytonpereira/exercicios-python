def celsius_p_f(c):
    return round(c * 1.8 + 32)

def f_p_celsius(f):
    return round((f - 32) * (5 / 9))


assert 21 == f_p_celsius(celsius_p_f(21)), 'Conversão correta'