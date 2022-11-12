from abc import ABCMeta, abstractmethod

class Programa(metaclass=ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @abstractmethod
    def __str__(self):
        pass


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
       return f'{self._nome} - {self.duracao} min: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.temporadas} temporadas: {self._likes}'


class Playlist:
    def  __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    #duck typing
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    todo_mundo_em_panico = Filme('todo mundo em panico', 1999, 100)

    atlanta = Serie('atlanta', 2018, 2)
    demolidor = Serie('demolidor', 2016, 2)

    todo_mundo_em_panico.dar_like()
    todo_mundo_em_panico.dar_like()
    todo_mundo_em_panico.dar_like()
    todo_mundo_em_panico.dar_like()

    vingadores.dar_like()

    demolidor.dar_like()
    demolidor.dar_like()

    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()

    print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
    print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')

    print(50*"#")
    filmes_e_series = [vingadores,atlanta, demolidor, todo_mundo_em_panico]
    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

    print(f'Nome da Playlist: {playlist_fim_de_semana.nome}')
    print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

    for programa in playlist_fim_de_semana:
        print(programa)
        #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
        #print(f'{programa.nome} - {detalhes}: {programa.likes}')


    print(f'ta ou nao ta? {demolidor in playlist_fim_de_semana}')

    print(playlist_fim_de_semana[0])