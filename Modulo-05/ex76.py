import json
from pathlib import Path

arquivo = Path('Arquivos') / 'ex76.json'

configuracao = {'volume': 81, 'bateria': 60, 'brilho': 50, 'teclado': 'ABNT2'}

with open(arquivo, 'w') as f:
    configuracao = json.dump(configuracao, f, sort_keys=True, indent=4)
    
with open(arquivo, 'r') as f:
    configuracao = json.load(f)

configuracao['volume'] = 80

with open(arquivo, 'w') as f:
    configuracao = json.dump(configuracao, f, sort_keys=True, indent=4)