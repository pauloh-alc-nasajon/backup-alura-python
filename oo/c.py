# Function defined outside the class
def f1(self, x, y):
    return min(x,x+y)

class C:
    f = f1

    def g(self):
        return 'Hello world'

    h = g

    # Agora , f, g e h sao atributos da classe C que reefrencia funcoes,
    # Mas essa pratica so serve para confundir

instancia = C()
print(instancia.f(2,3))
print(instancia.g())