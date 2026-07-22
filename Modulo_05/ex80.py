from pathlib import Path
import random
from Modulo_04.ex60 import eh_primo

arquivo = Path(__file__).parent / 'Arquivos' / 'ex80'

with open(arquivo, 'a') as f:
    for x in range(100):
        numero = random.randint(1, 200)
        escrever = f.write(f'{numero}\n')

with open(arquivo, 'r') as f:
    conteudo = f.readlines()

for x in conteudo:
    if eh_primo(int(x)):
        print(f'O numero {x.replace('\n', '')} é primo')
    else:
        print(f'O numero {x.replace('\n', '')} não e primo')