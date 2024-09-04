from classes import Player as p, IAPlayer as ia


if __name__ == '__main__':
    p_ia = ia()
    while True:
        try:
            p1 = p(input("\nInforme seu nome: "))
            break
        except TypeError as e:
            print(str(e).capitalize() + "\n" + "Tente novamente!")
            continue

    for t in range(3):
        # validação da entrada do usuário para uma opção
        while True:
            try:
                choice = int(input("\nTabela de Ações:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n\nEscolha sua ação: "))
            except ValueError:
                print("\nValueError: a opção do jogador deve ser um número inteiro")
                continue
            print(f"Escolha da IA: {p_ia.choiceIA()}")
            try:
                p1.choice = choice
                break
            except ValueError or TypeError as e:
                print("\n" + str(e))
                continue

        p.duel(p1, p_ia)
        print("\n" + p.scoreboard(p1, p_ia))
    else:
        p.final_scoreboard(p1, p_ia)
