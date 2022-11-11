
class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sorenome = sobrenome

    def exie_nome_e_sobrenome(self):
        print("{0} {1}".format(self.nome, self.sorenome))

