from exceptions import SaldoInsuficienteError, OperacaoFinaceiraError


class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente=None, agencia=0, numero=0):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0

        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidas = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo agencia deve ser um inteiro', value)
        if value <= 0:
            raise ValueError("O atributo agencia deve ser maior que Zero")
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo numero deve ser um inteiro')
        if value <= 0:
            raise ValueError('O atributo numero deve ser maior que Zero')
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo saldo deve ser um inteiro')
        if value < 0:
            raise ValueError('O saldo deve ser maior que Zero')

        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError('O valor a ser transferido nao poder ser menor que Zero')

        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            import traceback
            self.transferencias_nao_permitidas += 1

            E.args = ()
            #traceback.print_exc()
            raise OperacaoFinaceiraError('Operacao nao finalizada') from E

        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError('O valor a ser sacado nao poder ser menor que Zero')
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError('', self.saldo, valor, 'arg1', 'arg2')
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo = self.saldo + valor


def main():
    import sys

    contas = []

    while True:
        try:
            nome = input("Nome do cliente:\n")
            agencia = input("Numero de agencia:\n")
            breakpoint()
            numero = input("Numero da conta corrente:\n")
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except KeyboardInterrupt:
            print(f"\n\n{len(contas)}(s) contas criadas")
            sys.exit()

# if __name__ == '__main__':
#     main()

try:

    conta_corrente1 = ContaCorrente(None, 400, 123456)
    conta_corrente2 = ContaCorrente(None, 401, 1234564)
    conta_corrente1.transferir(105, conta_corrente2)
    print(conta_corrente1.saldo)
    print(conta_corrente2.saldo)
    # conta_corrente1.sacar(110)
    # print(conta_corrente1.saldo)

except OperacaoFinaceiraError as E:
    # breakpoint()
    pass

    # import traceback
    # print(E.args)
    # print(E.saldo)
    # print(E.valor)
    # print('Excecao do tipo ', E.__class__)
    # print('Excecao do tipo ', E.__class__.__name__)
    # traceback.print_exc()


