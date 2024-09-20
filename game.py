from player import Player as p, IAPlayer as ia


class Game:
    def __init__(self, player):
        self.turn = 0
        self.ia = ia()
        self.__player = player if isinstance(player, p) else TypeError(f"player has to be an instance of Player, instead is: {type(player)}")

    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, value):
        if isinstance(value, p):
            self.__player = value

    def duel(self):
        if (self.player.choice == 1 and self.ia.choice == 3) or (self.player.choice > self.ia.choice):
            self.player.wins += 1
        elif (self.ia.choice == 1 and self.player.choice == 3) or (self.ia.choice > self.player.choice):
            self.ia.wins += 1

    def scoreboard(self, is_final=False):
        # função que retorna um placar formatado comparando as vitórias de 2 jogadores, tipo: str
        hor_line = f"|{'-' * 25}|"
        label = f"|{'Placar:'.center(25)}|"
        score = f"|{f'{self.player.name}: {self.player.wins} {self.ia.name}: {self.ia.wins}'.center(25)}|"

        if is_final:
            final_label = f"|{'Placar Final:'.center(25)}|"
            if self.player.wins > self.ia.wins:
                return hor_line + "\n" + final_label + "\n" + score + "\n" + hor_line + "\n\n" + f"Parabéns: {self.player.name}!"
        return hor_line + "\n" + label + "\n" + score + "\n" + hor_line