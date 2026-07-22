from pathlib import Path
import csv

mensagem = Path(__file__).parent / 'Arquivos' / 'mensagem.csv'
arquivo = Path(__file__).parent / 'Arquivos' / 'ex81.csv'
chaves = ['atraso', 'bug', 'bloqueado', 'esperando', 'impede', 'urgente']

with open(mensagem, 'a') as f:
    if mensagem.exists() and mensagem.stat().st_size == 0:
        escrever = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escrever.writerow(['Autor', 'Texto'])
        escrever.writerow(['Ana', 'Reunião de alinhamento marcada para amanhã às 10h'])
        escrever.writerow(['Bruno', 'Encontrei um bug no login que impede o usuário de entrar'])
        escrever.writerow(['Carla', 'O deploy foi concluído sem problemas ontem à noite'])
        escrever.writerow(['Ana', 'Estamos com atraso na entrega do módulo de pagamentos'])
        escrever.writerow(['Bruno', 'Documentação atualizada com os novos endpoints da API'])
        escrever.writerow(['Carla', 'O time está bloqueado esperando acesso ao servidor de staging'])
        escrever.writerow(['Ana', 'Testes automatizados passaram sem nenhuma falha'])
        escrever.writerow(['Bruno', 'Corrigido o bug de renderização no dashboard principal'])
        escrever.writerow(['Carla', 'Sprint planning ficou marcado para segunda-feira de manhã'])
        escrever.writerow(['Ana', 'Cliente relatou atraso na resposta do suporte técnico'])
        escrever.writerow(['Bruno', 'Revisão de código finalizada, pode seguir para merge'])
        escrever.writerow(['Carla', 'Estou bloqueado por falta de permissão no banco de dados'])
        escrever.writerow(['Ana', 'Reunião de retrospectiva foi bem produtiva essa semana'])
        escrever.writerow(['Bruno', 'Novo bug crítico encontrado em produção, precisa de atenção urgente'])
        escrever.writerow(['Carla', 'Ambiente de homologação funcionando normalmente'])
        escrever.writerow(['Ana', 'Projeto sofrendo atraso por causa de mudança de escopo'])
        escrever.writerow(['Bruno', 'Fiquei bloqueado tentando configurar o pipeline de CI/CD'])
        escrever.writerow(['Carla', 'Feature nova implementada e já disponível para testes'])
        escrever.writerow(['Ana', 'Identificado bug de performance na tela de relatórios'])
        escrever.writerow(['Bruno', 'Entrega do sprint concluída dentro do prazo previsto'])

with open(arquivo, 'a') as f:
    risco_escrever = csv.DictWriter(f, fieldnames=['Autor', 'Contagem', 'Texto'])
    
    if arquivo.exists() and arquivo.stat().st_size == 0:
        risco_escrever.writeheader()
    
    with open(mensagem, 'r') as documento:
        ler = csv.DictReader(documento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for dicionario in ler:  
            if any(sub.lower() in dicionario['Texto'].lower() for sub in chaves):
                cont = len([palavra for palavra in dicionario['Texto'].split() if palavra.lower() in chaves])
                risco_escrever.writerow({'Autor': dicionario['Autor'], 'Contagem': cont, 'Texto': dicionario['Texto']})