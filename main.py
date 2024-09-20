from game import Game
from player import Player as p, IAPlayer as ia


if __name__ == '__main__':

    # criação do jogador e da estrutura básica do jogo
    while True:
        try:
            p1 = p(input("\nInforme seu nome: "))
            break
        except TypeError as e:
            print(str(e).capitalize() + "\n" + "Tente novamente!")
            continue
        except ValueError as e:
            print(str(e).capitalize() + "\n" + "Tente novamente!")
    game = Game(p1)

    # geração de turnos do jogo, até encontrar o vencedor
    while (game.turn > 2 and game.player.wins == game.ia.wins) or (game.turn <= 2):
        # validação da entrada do usuário para uma opção
        print(f"\nTurno: {game.turn + 1}")
        while True:
            try:
                choice = int(input("\nTabela de Ações:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nEscolha sua ação: "))
                print(f"\nEscolha de {game.player.name}: {p.CHOICES[choice]}")
                print(f"Escolha da IA: {p.CHOICES[game.ia.choiceIA()]}")
            except ValueError:
                print("\nValueError: a opção do jogador deve ser um número inteiro")
                continue
            except KeyError:
                print("\nKeyError: a opção do jogador deve ser 1, 2 ou 3")
                continue
            try:
                game.player.choice = choice
                break
            except ValueError or TypeError as e:
                print("\n" + str(e))
                continue
        game.duel()
        if game.turn < 2 or (game.turn >= 2 and game.player.wins == game.ia.wins):
            print("\n" + game.scoreboard())
        game.turn += 1
    else:
        print("\n" + game.scoreboard(True))
