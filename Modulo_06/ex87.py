from dataclasses import dataclass
from Modulo_06.ex86 import Mensagem

@dataclass
class Risco:
    descricao : Mensagem
    categoria : str
    impacto : int

    def __post_init__(self):
        self.impacto = int(self.impacto)
        if not self.descricao.contem_risco:
           raise ValueError('Não é possivel adicionar') 

    def __str__(self) -> str:
        return f'----------------Risco----------------\nA categoria: {self.categoria}\nO impacto: {self.impacto}\n{self.descricao}'
