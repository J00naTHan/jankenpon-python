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
