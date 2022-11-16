from collections import Counter

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))

    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao  in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


analisa_frequencia_de_letras("Paulo Alencar")