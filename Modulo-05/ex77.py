from pathlib import Path
from datetime import date

arquivo = Path('Arquivos') / 'ex77'

while True:
    entrada = input('O que estudou hoje?\n')

    if entrada == 'Sair':
        break

    with open(arquivo, 'a') as f:
        f.write(f'{date.today()} - {entrada}\n')
        continue

with open(arquivo, 'r') as f:
    print(f.read())