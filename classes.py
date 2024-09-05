import random as rd


class GenericPlayer:
    CHOICES = {1: "pedra", 2: "papel", 3: "tesoura"}

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
            raise TypeError(f"tipo de dado inválido para o nome do jogador: {value}")
        else:
            if len(value) > 14:
                raise ValueError(f"nome de jogador deve ter um comprimento menor ou igual a 14 caracteres: {value}")
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
    def scoreboard(p1, p2, state=None):
        # função que retorna um placar formatado comparando as vitórias de 2 jogadores, tipo: str
        if not (isinstance(p1, GenericPlayer) and isinstance(p2, GenericPlayer)):
            raise TypeError("o placar deve ser criado para 2 jogadores")

        hor_line = f"|{'-' * 25}|"
        label = f"|{'Placar:'.center(25)}|"
        score = f"|{f'{p1.name}: {p1.wins} {p2.name}: {p2.wins}'.center(25)}|"

        if state == "final":
            final_label = f"|{'Placar Final:'.center(25)}|"
            if p1.wins > p2.wins:
                if p1.name != "IA":
                    return hor_line + "\n" + final_label + "\n" + score + "\n" + hor_line + "\n\n" + f"Parabéns: {p1.name}!"
            elif p2.wins > p1.wins:
                if p2.name != "IA":
                    return hor_line + "\n" + final_label + "\n" + score + "\n" + hor_line + "\n\n" + f"Parabéns: {p2.name}!"
        else:
            return hor_line + "\n" + label + "\n" + score + "\n" + hor_line


class Player(GenericPlayer):
    def __init__(self, name):
        super().__init__()
        self.name = name


class IAPlayer(GenericPlayer):
    def __init__(self):
        super().__init__()
        self.name = "IA"

    def choiceIA(self):
        choice = rd.randint(1, 3)
        self.choice = choice
        return choice
