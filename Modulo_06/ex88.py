from dataclasses import dataclass, field
from Modulo_06.ex87 import Risco

@dataclass
class RegistroDeRiscos():
    criticos : list[Risco] = field(default_factory=list)

    def adicionar(self, risco):
        self.criticos.append(risco)

    def __str__(self) -> str:
        return '\n'.join(str(x) for x in self.criticos)

    def por_categoria(self, cat) -> str:
        print('Aqui abaixo estão com a categoria correspondente')
        return '\n'.join(str(x) for x in self.criticos if x.categoria == cat)

    def mais_graves(self, n) -> str:
        print(f'Os {n} riscos mais graves de acordo com o impacto')
        lista_ordenada = reversed(sorted(self.criticos, key=lambda item: item.impacto))
        return '\n'.join(str(linha) for posicao, linha in enumerate(lista_ordenada, start=1) if posicao <= n) 