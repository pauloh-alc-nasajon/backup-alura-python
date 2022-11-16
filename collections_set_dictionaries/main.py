from collections import defaultdict, Counter

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

assistiram = set(assistiram)
print(assistiram)


print(set([1,2,3, 3]))

conjunto = {0,1,2,3,3,3,4,5,5,5,5,6} # Conjunto - Nao possui repeticoes, nem indexacao, eh mutavel
print(conjunto)


for elemento in set([1,2,2,2,2,2,3,4,5,6]):
    print(elemento)


# Uniao:
set1 = {0,1,2,3,4}
set2 = {3,4,5,6,7,8,-1}
print(set1 | set2)

#Intersecao:
print(set1 & set2)

#####################

usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))

usuarios.add(45)

print(usuarios)

# Congelando um SET
usuarios=frozenset(usuarios)
print(type(usuarios))

texto="Paulo , Ola meu nome eh Paulo , tenho 22 anos . Os anos que tenho, sao meus, afinal meu nome eh Paulo"
lista = texto.split()

print(set(lista)) # removendo a duplicidade

# Dicionario

dicionario = {
    "Guilherme": 1,
    "Cachoro": 2,
    "nome": 2,
    "vindo": 1
}

print(dicionario)
print(dicionario["Guilherme"]) # valor p/ chave Guilherme
print(dicionario["nome"])

print(dicionario.get("xpto", 0))
print(dicionario.get("nome", 0))

outro_dict = dict(Guilherme = 2, Paulo = 4, Palmeiras = 56)
print(outro_dict)

dicionario["PAULINHO"] = 45 # adicionando
print(dicionario)

dicionario["LISTA"] = [0,1,2,3,4,5,6]
print(dicionario)

del dicionario["LISTA"]

print("LISTA" in dicionario) # buscando pelas chaves
print("PAULINHO" in dicionario)


for elemento in dicionario:
    print(elemento)

for elemento in dicionario:
    print(dicionario[elemento])

for chaves in dicionario.keys():
    print(chaves)

for valores in dicionario.values():
    print(valores)

for item in dicionario.items():
    print(item)

for chave, valor in dicionario.items():
    print(chave," = ",valor)

list_comprehension = ["CHAVE: {}".format(chave) for chave in dicionario]
print(list_comprehension)

meu_text = texto.lower()
print(meu_text)

aparicoes = {}

for palavra in meu_text.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)


apa = defaultdict(int)
for palavra in meu_text.split():
    ate_agora = apa[palavra]
    apa[palavra] = ate_agora + 1

print(apa)

class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)
contas[15]

print(Counter(meu_text.split()))

print(sum({'oi': 2, 'a': 3}.values()))