class Relatorio:
    def gera_relatorio(self):
        print('Relatorio geral')


class RelatorioUsuarios(Relatorio):
    def gera_relatorio(self):
        print('Relatorios dos Usuarios')


class RelatorioCustos(Relatorio):
    def gera_relatorio(self):
        print('Relatorios de custos')


if __name__ == '__main__':
    relatorio1 = RelatorioUsuarios()
    relatorio2 = RelatorioCustos()
    relatorio3 = RelatorioUsuarios()
    relatorio4 = RelatorioUsuarios()

    relatorios = [relatorio1, relatorio2, relatorio3, relatorio4]

    for relatorio in relatorios:
        relatorio.gera_relatorio() # Polimorfismo ocorrendo