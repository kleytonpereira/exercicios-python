import csv
from pathlib import Path

def cadastra_pessoa():
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))

    if idade < 0:
        raise ValueError(f'Idade Negativa')
    
    return {'Nome': nome, 'Idade': idade}

arquivo = Path(__file__).parent / 'Arquivos' / 'ex82.csv'

while True:
    operacao = input('Caso deseja sair digite "1 - Sair", se não digite qualquer coisa): ')

    if operacao == '1':
        break
    
    with open(arquivo, 'a') as f:
        escrever = csv.DictWriter(f, fieldnames=['Nome', 'Idade'])

        if arquivo.exists() and arquivo.stat().st_size == 0:
            escrever.writeheader()

        try:
            escrever.writerow(cadastra_pessoa())
        except ValueError:
            print('Precisa digitar uma idade maior que 0')






