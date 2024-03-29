import random

def determine_vencedor(escolha_jogador, escolha_computador):
    if escolha_jogador == escolha_computador:
            return "Empate!"
    elif (
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura")or
            (escolha_jogador == "tesoura" and escolha_computador == "pepel")
        ):
         return "Você venceu!"
    else:
         return "Você perdeu!"

def jogar_jokenpo():
    opcoes = ["pedra", "papel","tesoura"]
    print("Bem-vindo ao jogo Jokenpô!")
    print("Escolha: pedra, papel ou tesoura.")
              
 
    while True:
        escolha_jogador = input("Sua escolha:")
        if escolha_jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        escolha_computador = random.choice(opcoes)

        print(f"computaor escolheu: {escolha_computador}")

        resultado = determine_vencedor(escolha_jogador,escolha_computador)
        print(resultado)

        if resultado == "Você ganhou!":
            vitorias += 1
        elif resultado == "Você perdeu!":
            vitorias -= 1 
        else:
            vitorias += 0 

        print(f"computador escolha")          

        if escolha_jogador == escolha_computador:
            print("Empate")
        elif(
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura")or
            (escolha_jogador == "tesoura" and escolha_computador == "pepel")):
            print("Você venceu!")
        else:
            print("Você perdeu!")


        jogar_novamente = input("Você quer jogar novamente?")
        if jogar_novamente != "sim":
            break                    




if __name__ == "__main__":
    jogar_jokenpo()
