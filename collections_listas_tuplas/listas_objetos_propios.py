class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)



if __name__ == '__main__':
    conta_do_gui = ContaCorrente(15)
    print(conta_do_gui)
    conta_do_gui.deposita(500)
    print(conta_do_gui)


    conta_da_dani = ContaCorrente(4884)
    conta_da_dani.deposita(1000)
    print(conta_da_dani)

    contas =  [conta_do_gui, conta_da_dani]