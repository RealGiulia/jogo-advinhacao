import random


def jogar():
    print("****************************************")
    print("Seja bem-vindo ao jogo de adivinhação!")
    print("****************************************")
    numero_secreto = random.randrange(0, 101)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel: int = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa", rodada, "de", total_de_tentativas)
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute: int = int(chute_str)
        chute = chute + 1
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break

        else:
            if menor:
                print("Voce errou! O numero secreto é maior do que seu chute.")
            elif maior:
                print("Voce errou! O numero secreto é menor do que seu chute.")
                pontos_perdidos = rodada
                pontos = pontos - pontos_perdidos


if __name__ == "__main__":
    jogar()
