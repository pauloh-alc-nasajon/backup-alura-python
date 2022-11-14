from listas_objetos_propios import ContaCorrente
# Tuplas - eh imutavel, costuma ser usado quando quero representar algo, onde cada posicao eh algo diferete
# Ex: (nome, idade, ano)
#     ('Paulo', 22, 2000)

def deposita_para_todos(contas):
    for conta in contas:
        conta.deposita(100)


if __name__ == "__main__":
    conta_do_gui = ContaCorrente(15)
    conta_do_gui.deposita(500)

    conta_da_dani = ContaCorrente(4884)
    conta_da_dani.deposita(1000)

    contas = [conta_do_gui, conta_da_dani]
    print(contas[0], contas[1])
    deposita_para_todos(contas)
    print(contas[0], contas[1])

    # contas.insert(0, 76)
    # print(contas[0], contas[1],contas[2])
    # deposita_para_todos(contas) # AttributeError: 'int' object has no attribute 'deposita'

    guilherme = ('Guilherme', 37, 1981)
    daniela = ('Daniela', 31, 1987)
    # paulo = (39, 'Paulo', 1979) # ruim


    def deposita(conta): # variacao "funcional" (separando o comportamento dos dados)
        novo_saldo = conta[1] + 100
        codigo = conta[0]

        return (codigo, novo_saldo) # retornado um tupla

    conta_do_gui = (15, 1000)
    # conta_do_gui.append(5) tupla eh imutavel

    print(conta_do_gui)
    conta_do_gui = deposita(conta_do_gui)
    print(conta_do_gui)


    usuarios = [guilherme, daniela]
    print(usuarios)
    usuarios.append(('Paulo', 39, 1979))