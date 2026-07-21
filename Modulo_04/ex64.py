def media(*notas):
    return sum(notas) / len(notas)

assert media(2, 4, 6) == 4, 'Media correta'
assert media(8, 8, 9, 9) == 8.5, 'Media correta'