def filtro_riscos(mensagens, palavras_chaves):
    return ([mensagem for mensagem in mensagens if any(palavra in mensagem for palavra in palavras_chaves)])

assert filtro_riscos(['Havera um atraso', 'Estamos com um bug', 'Projeto esta otimo', 'Isso gera um bloqueio', 'A comunicação esta otima'], 
                    ['bloqueio', 'bug', 'atraso']) == ['Havera um atraso', 'Estamos com um bug', 'Isso gera um bloqueio'], 'Não passou'