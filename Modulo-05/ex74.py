import csv
from pathlib import Path

pasta = Path('Arquivos')
arquivo = pasta / 'ex74'

with open(arquivo, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['data', 'categoria', 'valor'])
    spamwriter.writerow(['19-07', 'comida', '19,28'])
    spamwriter.writerow(['20-07', 'comida', '30,50'])
    spamwriter.writerow(['20-07', 'transporte', '50,00'])
    spamwriter.writerow(['21-07', 'comida', '5,79'])


cont = dict()
with open(arquivo, 'r', newline='') as csvfile:
        documento = csv.DictReader(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for linha in documento:
            if (linha['categoria']) not in cont:
                 cont[linha['categoria']] = float(linha['valor'].replace(',', '.'))
            else:
                 cont[linha['categoria']] += float(linha['valor'].replace(',', '.'))
            

        

