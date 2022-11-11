class Bag:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def addtwice(self, value):
        self.add(value)
        self.add(value)

bag1 = Bag()
bag1.add('Blusa')
bag1.addtwice('Camiseta')
print(bag1.data)