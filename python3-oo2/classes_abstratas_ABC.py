# Abstract base classes
from abc import ABC

from collections.abc import MutableSequence
from numbers import Complex

class Playlist(MutableSequence):
    pass


# filmes = Playlist()


class Numero(Complex):
    pass

instancia = Numero()
