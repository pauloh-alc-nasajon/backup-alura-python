class OperacaoFinaceiraError(Exception):
    pass


class SaldoInsuficienteError(OperacaoFinaceiraError):
    def __init__(self, mensagem='', saldo=None, valor=None, *args, **kwargs):
        self.saldo = saldo
        self.valor = valor
        self.teste = 450
        msg = 'Saldo insuficiente para efetuar a transacao\n' \
            f'Saldo atual: {self.saldo} Valor a ser sacado: {self.valor}'
        self.msg = mensagem or msg

        super(SaldoInsuficienteError, self).__init__(self.msg, saldo, valor, *args)