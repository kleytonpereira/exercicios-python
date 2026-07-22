class ContaBancaria():
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, numero):
        self.saldo += numero
        print(self.saldo)
        return self.saldo

    def sacar(self, numero):
        if self.saldo - numero  < 0:
            raise ValueError('Valor não pode ficar negativo')
        
        self.saldo -= numero
        return self.saldo
    
try:
    conta = ContaBancaria(100)
    conta.depositar(50)
    print(conta.saldo)
    print(ContaBancaria(100).depositar(50))
    assert ContaBancaria(100).depositar(100) == 200, 'Deposito calculado incorretamente'
    assert ContaBancaria(150).sacar(50) == 100, 'Saque calculado incorretamente'
    assert ContaBancaria(50).sacar(100), 'Salque calculado incorretamente'
except ValueError:
    print('Não é possivel sacar mais que o saldo da sua conta')