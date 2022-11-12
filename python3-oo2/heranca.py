class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas ...')

    def mostrar_tarefas(self):
        print('Fez muita coisa ...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mes')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas nao respondidas do forum')


# Heranca normal
class Junior(Alura):
    pass

# Heranca multipla
class Pleno(Alura, Caelum):
    pass

#  Mixins --> apenas classes que podem ser herdadas mas que não devem ser instanciadas, já que servem para disponibilizar comportamentos para outras classes.
class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Senior(Alura, Caelum, Hipster):
    pass

jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()
print('#################')
luan = Pleno('Laun')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes('janeiro')
luan.mostrar_tarefas()

# MRO - algoritmo
# Pleno --> Alura --> Funcionario --> Caelum --> Funcionario
# O algoritmo(MRO) remove as repeticoes

senior = Senior('Formiga')
print(senior)