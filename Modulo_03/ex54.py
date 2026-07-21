idades = [52, 88, 44, 54, 84, 34, 55, 16, 19, 24, 16, 68, 74, 13, 70, 52, 32, 18, 21, 66, 48, 64, 78, 65, 37]

faixas = {'menores': [],   'adultos': [],  'idosos': []}

for idade in idades:
    if 0 < idade < 18:
        faixas['menores'].append(idade)
    elif idade < 55:
        faixas['adultos'].append(idade)
    else:
        faixas['idosos'].append(idade)

print(faixas)    