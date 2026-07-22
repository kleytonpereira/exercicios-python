import json
from pathlib import Path

pasta = Path(__file__).parent / 'Arquivos' / 'issues_fake'
criticos = []

for arquivo in pasta.rglob('*'):
    if arquivo.is_file():
        with open(arquivo, 'r') as f:
            arquivo_aberto = json.load(f)

            if arquivo_aberto['prioridade'] in ('Blocker', 'Critical'):
                criticos.append(arquivo_aberto)

criticos = sorted(criticos, key=lambda item: item['id'])
print(criticos)