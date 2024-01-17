# Template method is pretty much
# the same as strategy but
# it uses inheritance not composite approach
# It creates a skeleton of an algorithm
# with specific methods realization in
# predefined subclasses
from abc import ABC


# Template method as it is
# Parent abstract class with some major predefined methods/attributes
# However, other methods are defined in subclasses, e.g. `class Chess`
class Game(ABC):
    def __init__(self, number_of_players):
        self.current_player = 0
        self.number_of_players = number_of_players

    def run(self):
        self.start()
        while not self.has_winner:
            self.take_turn()
        print(f'Player {self.winning_player} wins')

    def start(self): pass

    def take_turn(self): pass

    @property
    def has_winner(self): pass

    @property
    def winning_player(self): pass


class Chess(Game):
    MAX_TURNS = 10
    NUMBER_OF_PLAYERS = 2

    def __init__(self):
        super().__init__(Chess.NUMBER_OF_PLAYERS)
        self.turn = 1

    def start(self):
        print(f'Starting a game of chess with \
              {Chess.NUMBER_OF_PLAYERS} players')

    def take_turn(self):
        print(f'Turn {self.turn} taken by {self.current_player}')
        self.turn += 1
        self.current_player = 1 - self.current_player  # 0 or 1

    @property
    def has_winner(self):
        return self.turn >= Chess.MAX_TURNS

    @property
    def winning_player(self):
        return self.current_player


if __name__ == '__main__':
    chess = Chess()
    chess.run()
