from player import Player as p, IAPlayer as ia


if __name__ == '__main__':

    # criação do jogador e da ia para o jogo
    p_ia = ia()
    while True:
        try:
            p1 = p(input("\nInforme seu nome: "))
            break
        except TypeError as e:
            print(str(e).capitalize() + "\n" + "Tente novamente!")
            continue
        except ValueError as e:
            print(str(e).capitalize() + "\n" + "Tente novamente!")

    # geração de turnos do jogo, até encontrar o vencedor
    turn = 1
    while (turn > 3 and p1.wins == p_ia.wins) or (turn <= 3):
        # validação da entrada do usuário para uma opção
        print(f"\nTurno: {turn}")
        while True:
            try:
                choice = int(input("\nTabela de Ações:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nEscolha sua ação: "))
                print(f"\nEscolha de {p1.name}: {p.CHOICES[choice]}")
                print(f"Escolha da IA: {p.CHOICES[p_ia.choiceIA()]}")
            except ValueError:
                print("\nValueError: a opção do jogador deve ser um número inteiro")
                continue
            except KeyError:
                print("\nKeyError: a opção do jogador deve ser 1, 2 ou 3")
                continue
            try:
                p1.choice = choice
                break
            except ValueError or TypeError as e:
                print("\n" + str(e))
                continue
        p.duel(p1, p_ia)
        if turn < 3 or (turn >= 3 and p1.wins == p_ia.wins):
            print("\n" + p.scoreboard(p1, p_ia))
        turn += 1
    else:
        print("\n" + p.scoreboard(p1, p_ia, "final"))
