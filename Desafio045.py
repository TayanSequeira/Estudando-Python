import random

rejogar = True
while rejogar:
    jogador = input("Vamos jogar pedra, papel e tesoura? (s/n) ")

    if jogador.lower() == "s":
        opcoes = ["pedra", "papel", "tesoura"]
        computador = random.choice(opcoes)
        nova_opcao = True

        while nova_opcao:
            jogador = input("Escolha pedra, papel ou tesoura: ")

            if jogador.lower() not in opcoes:
                print("Escolha inválida.")
            else:
                print('O jogador escolheu {}'.format(jogador.lower()))
                print('Eu máquina escolhi {}'.format(computador))

                if jogador.lower() == computador:
                    print('Empatamos U.u')
                elif jogador.lower() == 'pedra' and computador == 'tesoura':
                    print('Parabéns você ganhou SEU LIXO')
                elif jogador.lower() == 'papel' and computador == 'pedra':
                    print('Parabéns você ganhou SEU LIXO')
                elif jogador.lower() == 'tesoura' and computador == 'papel':
                    print('Parabéns você ganhou SEU LIXO')
                else:
                    print('Tu é muito ruim, ganhei :P')

                nova_opcao = False

        jogar_denovo = input("Quer jogar novamente? (s/n) ")
        if jogar_denovo.lower() != "s":
            rejogar = False
    elif jogador.lower() == 'n':
        rejogar = False
        print('Eu iria ganhar mesmo :P')
    else:
        print('Não reconheço essa reposta')