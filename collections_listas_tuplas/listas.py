# Trabalhando com listas - lembranddo que listas sao mutaveis
idades = [39, 30, 27, 18]

print(type(idades))

print(len(idades))

print(idades[0])

print(idades)

idades.append(15)

print(idades)

# print(idades[5]) # IndexError: index out of range

for idade in idades:
    print(idade)

# idades.remove(100) # ValueError: list.remove(x):x not in list

idades.remove(15)
print(idades)

# O list.append(x) equivale: lista[len(lista):] = [x]

idades[len(idades):] = [45]
print(idades)

# idades.clear() # Equivale a del idades[:]
print(idades)

print(28 in idades)
print(15 in idades)

if 15 in idades:
    idades.remove(15)

idades.insert(0, 19)
print(idades)

idades.extend([99, 88]) # Equivale a[len(a):] = iterable
print(idades)

# List Comprehension:

list_comprehesion = [idade+1 for idade in idades]
print(list_comprehesion)

idades_maiores_21 = [idade + 1 for idade in idades if idade > 21]
print(idades_maiores_21)

def retorna_idade_daqui_10(idade):
    return idade + 10

new_idades = [retorna_idade_daqui_10(idade) for idade in idades]
print(new_idades)

#################################################################

# Cuidado com objetos mutaveis:..............
def faz_processamento_de_visualizacao(lista = []):
    print(len(lista))
    lista.append(15)

minhas_idades = [16,21,29,56,43]
faz_processamento_de_visualizacao(minhas_idades)
print(minhas_idades)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()


def faz_processamento_de_visualizacao(lista=None):
    if lista == None:
        lista = list()

    print(len(lista))
    lista.append(15)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()