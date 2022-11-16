from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.cliente = cliente
        self.__agencia = agencia
        self.__numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            print("O atributo agencia deve ser maior que Zero")
            return
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return

        print('Saldo anterior: ', self.__saldo)
        self.__saldo = value

    def transfeir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo = self.saldo + valor


cliente = Cliente('Paulo', '068.175.955-09', 'Desenvolvedor')
pprint(cliente.__dict__, width=40)

cliente.idade = 22
print(cliente.idade)

try:
    conta = ContaCorrente(cliente, 100, 2550)
except ValueError as E:
    print(E)
    print("Algum valor incorreto foi inserido no construtor")
except AttributeError:
    print('caiu')


# conta.agencia = 0
print(conta.saldo)
