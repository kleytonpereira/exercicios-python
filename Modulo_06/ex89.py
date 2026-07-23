class Funcionario():
    def __init__(self, nome, salario=1500):
        self.nome = nome
        self.salario = float(salario)

    def bonus_ano(self):
        return self.salario * 1.10
    

class Gerente(Funcionario):
    def __init__(self, nome, salario=1500):
        super().__init__(nome, salario)
        

    def bonus_ano(self):
        return self.salario * 1.25
    

pessoa = Funcionario('Kleyton', '2000')
print(pessoa.bonus_ano())
gerente = Gerente(pessoa.nome, pessoa.salario)
print(gerente.bonus_ano())
