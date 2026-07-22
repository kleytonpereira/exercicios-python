class Mensagem():
    def __init__(self, autor, texto, timestamp):
        self.autor = autor
        self.texto = texto
        self.timestamp = timestamp

    def contem_risco(self, *palavras):
        return any(x.lower() in self.texto.lower() for x in palavras)
    

assert Mensagem('Kleyton', 'Se continuar assim vai haver um bloqueio', '2026-07-22 15:30:45').contem_risco('Bloqueio', 'Risco', 'Atrasado'), 'Não esta realizando a identificação'