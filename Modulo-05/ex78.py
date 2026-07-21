import json
from pathlib import Path

arquivo = Path('Arquivos') / 'ex78.json'
    
try:
    with open(arquivo, 'r') as f:
        configuracao = json.load(f)
except FileExistsError:
    print("Erro: O arquivo não foi encontrado.")
except FileNotFoundError:
    print('Não foi encontrado o arquivo no diretorio')
except json.JSONDecodeError as e:
    print(f"Erro: JSON inválido na linha {e.lineno}, coluna {e.colno}: {e.msg}")