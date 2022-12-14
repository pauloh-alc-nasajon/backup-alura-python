class Dog:

    kind = 'canine' # class variable shared by all instance
    #tricks = []     # mistaken use of a class variable

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)   # shared by all dogs
print(e.kind)   # shared by all dogs

print(d.name)   # unique to d
print(e.name)   # unique to e

d.add_trick('rool over')
e.add_trick('play dead')

print(d.tricks) 
print(e.tricks)