from pathlib import Path

pasta = Path('Arquivos')
arquivo = pasta / 'ex72'

pasta.mkdir(parents=True, exist_ok=True)

with open(arquivo, 'w') as f:
    for x in range(1, 11):
        f.write(f'Escrevendo no arquivo\n')

with open(arquivo, 'r') as f:
    conteudo = f.readlines()
    
for posicao, linha in enumerate(conteudo, start=1):
    print(f'Linha {posicao} - {linha}', end='')