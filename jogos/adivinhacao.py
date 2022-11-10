import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhacao")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas= 3
    rodada = 1
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) facil (2) medio (3) Dificil")
    nivel  = int(input("Defina um nivel:"))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu numero entre  1 e 100: ")
        print("Voce digitou", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Voce acertoue fez {pontos} pontos")
            break
        else:
            if maior:
                print("Voce errou! o seu chute foi maior que o numero secreto", end="\n\n")
            elif menor:
                print("Voce errou! o seu chute foi menor que o numero secreto", end="\n\n")

            pontos_perdidos= abs(numero_secreto - chute)
            pontos = pontos- pontos_perdidos

            if rodada == total_de_tentativas:
                print("O numero secreto era {}. Voce fez {}".format(numero_secreto, pontos))

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
