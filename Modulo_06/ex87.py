class Risco():
    def __init__(self, categoria, descricao, impacto):
        self.descricao = descricao
        self.categoria = categoria
        self.impacto = int(impacto)

    def __str__(self):
        return f'A categoria: {self.categoria}\nA descrição: {self.descricao}\nO impacto: {self.impacto}'
