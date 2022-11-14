from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

class ContaMultiploSalario(ContaSalario):
    pass

if __name__ == "__main__":
    conta1 = ContaSalario(37)
    print(conta1)

    conta2 = ContaSalario(37)
    print(conta2)

    print(conta1 == conta2)

    contas = [conta1]
    print(conta1 in contas)
    print(conta2 in contas)


    print('#'*30)

    conta_m = ContaMultiploSalario(37)

    print(conta_m == conta1)

    print(conta1 < conta2)
    print(conta1 <= conta2)
    print(conta1 >= conta1)
