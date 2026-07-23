from Modulo_06.ex87 import Risco

class RegistroDeRiscos():
    def __init__(self):
        self.criticos = []

    def adicionar(self, risco):
        self.criticos.append(risco)

    def __str__(self):
        return '\n'.join(str(x) for x in self.criticos)

    def por_categoria(self, cat):
        print('Aqui abaixo estão com a categoria correspondente')
        return '\n'.join(str(x) for x in self.criticos if x.categoria == cat)

    def mais_graves(self, n):
        print(f'Os {n} riscos mais graves de acordo com o impacto')
        lista_ordenada = reversed(sorted(self.criticos, key=lambda item: item.impacto))
        return '\n'.join(str(linha) for posicao, linha in enumerate(lista_ordenada, start=1) if posicao <= n) 

registro = RegistroDeRiscos()

while True:
    operacao = input('Digite o que quer fazer (1 - Adicionar | 2 - Filtrar por categoria | 3 - Mais criticos):')
    if operacao == '1':
        categoria = input('Digite a categoria do risco: ')
        descricao = input('Digite a descrição do risco: ')
        impacto = input('Digite o impacto do risco: ')
        registro.adicionar(Risco(categoria, descricao, impacto))
    elif operacao == '2':
        categoria = input('Digite a categoria que deseja filtrar: ')
        print(registro.por_categoria(categoria))
    elif operacao == '3':
        critico = input('Digite quantos riscos criticos deseja ver do projeto: ')
        print(registro.mais_graves(int(critico)))
    else:
        print('Operação invalida, tente novamente')