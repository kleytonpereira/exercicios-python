capital = float(input('Qual é a quantidade de capital inicial: '))
taxa = float(f'1.' + input('A taxa de juto esta em quanto %: '))
meses = int(input('Quanto meses esse dinheiro vai ficar parado?: '))
aporte_mensal = float(input('Qual vai ser o aporte mensal além do capital inicial?: '))

for x in range(meses):
    if x == 0:
        capital *= taxa
        continue

    capital += aporte_mensal
    capital *= taxa

print(capital)