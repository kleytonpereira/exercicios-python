class Funcionario():
    def __init__(self, nome, salario=1500):
        self.nome = nome
        self.salario = float(salario)

    @property
    def bonus_ano(self) -> float:
        return self.salario * 1.10
    

class Gerente(Funcionario):
    def __init__(self, nome, salario=1500):
        super().__init__(nome, salario)
        

    def bonus_ano(self) -> float:
        return self.salario * 1.25