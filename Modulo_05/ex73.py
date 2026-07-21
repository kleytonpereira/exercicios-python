from pathlib import Path

cont = {'linhas': 0, 'palavras': 0, 'caracteres': 0}
pasta = Path('Arquivos')
arquivo = pasta / 'ex72'

with open(arquivo, 'r') as f:
    conteudo = f.readlines()

cont['linhas'] = len(conteudo)

for linha in conteudo:
    cont['palavras'] += len(linha.split())
    cont['caracteres'] += len(linha)

print(cont)