from dataclasses import dataclass

@dataclass
class Mensagem:
    autor : str
    texto : str
    timestamp : str

    @property
    def contem_risco(self) -> bool:
        return any(x.lower() in self.texto.lower() for x in ['Bloqueio', 'Atraso', 'Bug', 'Impedimento', 'Perigo', 'Alinhamento'])
    
    def __str__(self) -> str:
        return f'----------------Mensagem----------------\nAutor: {self.autor}\nTexto da mensagem: {self.texto}\nMomento que foi gerado: {self.timestamp}'