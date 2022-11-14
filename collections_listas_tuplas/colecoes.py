from contasalario import ContaSalario
from operator import attrgetter

idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])


print(range(len(idades))) # lazy
print(enumerate(idades))  # lazy

print(list(range(len(idades)))) # forcei a geracao dos valores
print(list(enumerate(idades))) # idem

for valor in enumerate(idades):
    print(valor)

# Fazer o desempacotamento:

for index, idade in enumerate(idades): # unpacking de nosssa tupla
    print(index, idade)


usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 37, 1979)
]

for usuario in usuarios:
    print(usuario)

for nome, idade, nascimento in usuarios:
    print(nome)


for _, _, nascimento in usuarios:
    print(nascimento)

for nome, _, _ in usuarios: # ja desempacotando, ignorando o resto
    print(nome)

# sorted -> para fazer a ordenacao sem mudar o conteudo na lista original
# reversed -> inverte os valores de uma lista sem alterar a lista original
# sort-> ordena, atribuindo e mudando a lista original

print(sorted(idades)) # Devolve uma lista ordenada
print(sorted(idades, reverse=True))
print(idades)
idades.sort() # como a lista eh mutavel, em todos os ponto do meu programa vou ter minha lista ordenada (além de ordenar, atribui o valor à lista original)
print(idades)


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
    print(conta)


def extrai_saldo(conta):
    return conta._saldo  # acessei um atributo privado :(

print(sorted(contas, key=extrai_saldo))
for conta in sorted(contas, key=extrai_saldo):
    print(conta)
print('############################')
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)


print(conta_do_paulo < conta_do_guilherme)
print(conta_do_guilherme < conta_da_daniela)

print('############################')
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")): # Primeiro ordena pelo saldo, depois pelo codigo
    print(conta)