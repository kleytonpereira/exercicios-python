class Risco():
    def __init__(self, descricao, categoria, impacto):
        self.descricao = descricao
        self.categoria = categoria
        self.impacto = impacto

    def __str__(self):
        return f'A categoria: {self.categoria}\nA descrição: {self.descricao}\nO impacto: {self.impacto}'


r = Risco('Uma pequena descrição', 'Tecnico', 'Atraso de homologação')
print(r)