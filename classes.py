import random as rd


class GenericPlayer:
    CHOICES = {1: "rock", 2: "paper", 3: "scissor"}

    def __init__(self):
        self.__name = None
        self.__choice = None
        self.__wins = 0

    # getters e setters definidos na superclasse

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            if value is not None:
                raise TypeError(f"tipo de dado inválido para o nome do jogador: {value}")
            else:
                self.__name = "IA"
            raise TypeError(f"tipo de dado inválido para o nome do jogador: {value}")
        else:
            self.__name = value

    @property
    def choice(self):
        return self.__choice

    @choice.setter
    def choice(self, value):
        if isinstance(value, int):
            if value in [1, 2, 3]:
                self.__choice = value
            else:
                raise ValueError("a opção do jogador deve ser um inteiro de 1 a 3")
        else:
            raise TypeError("a opção do jogador deve ser um número inteiro")

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        if isinstance(value, int):
            if value in range(0, 4):
                self.__wins = value
            else:
                raise ValueError("o número de vitórias do jogador deve ser um inteiro entre 0 e 3")
        else:
            raise TypeError("o número de vitórias do jogador deve ser um número inteiro")

    # métodos estáticos definidos na superclasse, definidos como estáticos por coesão sintática

    @staticmethod
    def duel(p1, p2):
        if not (isinstance(p1, GenericPlayer) and isinstance(p2, GenericPlayer)):
            raise TypeError("um duelo deve ser disputado entre 2 jogadores")
        if (p1.choice == 1 and p2.choice == 3) or (p1.choice > p2.choice):
            p1.wins += 1
        elif (p1.choice == 3 and p2.choice == 1) or (p2.choice > p1.choice):
            p2.wins += 1

    @staticmethod
    def scoreboard(p1, p2):
        # função que retorna um placar formatado comparando as vitórias de 2 jogadores, tipo: str

        if not (isinstance(p1, GenericPlayer) and isinstance(p2, GenericPlayer)):
            raise TypeError("o placar deve ser criado para 2 jogadores")

        top_padding = f"|{''.center(24, '-')}|"
        label = f"|{'Placar:'.center(18)}|"
        score = f"{p1.name}: {p1.wins} {p2.name}: {p2.wins}"
        score_string = f"|{score.center(int(24 - (len(score) / 2)))}|"
        bottom_padding = f"|{''.center(24, '-')}|"

        return top_padding + "\n" + label + "\n" + score_string + "\n" + bottom_padding

    @staticmethod
    def final_scoreboard(p1, p2):
        # mesmo que o de cima, mas formatado para o placar final
        pass


class Player(GenericPlayer):
    def __init__(self, name):
        super().__init__()
        self.name = name


class IAPlayer(GenericPlayer):
    def __init__(self):
        super().__init__()

    def choiceIA(self):
        choice = rd.randint(1, 3)
        self.choice = choice
        return choice
