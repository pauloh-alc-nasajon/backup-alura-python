

class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Contruindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    # Helper method
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <=  valor_disponivel_para_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite'.format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # Getters and Setters
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Static method
    @staticmethod
    def codigo_banco():
        return "001"

    # Static method
    @staticmethod
    def codigos_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    