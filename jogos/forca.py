import random
import os


def imprimir_mensagem_abertura():
    print("********************************")
    print("***Bem vindo ao jogo da Forca***")
    print("********************************")


def carregar_palavra_secreta(nome_do_arquivo="./temas/linguagens.txt", primeira_linha_valida=0):
    arquivo = open(nome_do_arquivo, 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializar_palavra_secreta(palavra):
    return ["_" for _ in palavra]


def obter_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute


def verificar_chute_correto(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1


def obter_nome_dos_arquivos():
    pasta = './temas'
    for dir in os.walk(pasta):
        arquivos = dir[2]

    return arquivos


def obter_opcao(arquivos):
    i = 0
    for arquivo in arquivos:
        i += 1
        print(f'{i}) {arquivo}')

    while True:
        op = int(input("Qual arquivo deseja carregar?"))
        if op <= 0 or op > len(arquivos):
            continue
        break

    return op - 1


def escolher_tema():
    arquivos = obter_nome_dos_arquivos()
    op = obter_opcao(arquivos)
    return arquivos[op]


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprimir_msg_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprimir_msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def jogar():
    imprimir_mensagem_abertura()
    arquivo = escolher_tema()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_palavra_secreta(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    max_erros = 7

    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = obter_chute()

        if chute in palavra_secreta:
            verificar_chute_correto(palavra_secreta, letras_acertadas, chute)
        else:
            erros += 1
            print("Voce errou, faltam {} tentativas".format(max_erros - erros))
            desenhar_forca(erros)

        enforcou = erros == max_erros
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprimir_msg_ganhador()
    else:
        imprimir_msg_perdedor(palavra_secreta)


if __name__ == "__main__":
    jogar()
