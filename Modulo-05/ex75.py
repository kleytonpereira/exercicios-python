import csv
from pathlib import Path

pasta = Path('Arquivos')
arquivo = pasta / 'ex74'
arquivo_2 = pasta / 'ex75'

cont = dict()
with open(arquivo, 'r', newline='') as csvfile:
        documento = csv.DictReader(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open(arquivo_2, 'r', newline='') as f:
              documento_2 = csv.DictReader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              verificar = list(documento_2)
        
        for linha in documento:
            if float(linha['valor'].replace(',', '.')) >  20.0:
                 with open(arquivo_2, 'a', newline='') as f:
                       escrever = csv.DictWriter(f, fieldnames=['data', 'categoria', 'valor'])

                       if arquivo_2.exists() and arquivo_2.stat().st_size == 0:
                            escrever.writeheader()
                       
                       if linha not in verificar:
                            escrever.writerow(linha)