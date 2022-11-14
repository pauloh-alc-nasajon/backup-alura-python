# Heranca e Polimorfismo:
from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta): # Classe abstrata
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod # Todo0 mundo vai ser obrigado a implementar
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


if __name__  == "__main__":
    conta16 = ContaCorrente(16)
    conta16.deposita(1000)
    conta16.passa_o_mes()
    print(conta16)

    conta17 = ContaPoupanca(17)
    conta17.deposita(1000)
    conta17.passa_o_mes()
    print(conta17)

    #########################

    conta16 = ContaCorrente(16)
    conta16.deposita(100)
    conta17 = ContaPoupanca(17)
    conta17.deposita(1000)

    # Polimorfismo:
    contas = [conta16, conta17] # lista de objetos de tipos diferentes
    for conta in contas:
        conta.passa_o_mes() #duck typing
        print(conta)


    #conta7 = ContaInvestimento(7)


    print(isinstance(ContaCorrente(45), Conta)) # Um objeto do tipo Filho, eh do tipo pai/mae
    print(isinstance(ContaCorrente(41), ContaCorrente))



