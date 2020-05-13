# from Player import Player
from RandomPlayer import RandomPlayer

# Right now, AIPlayer inherits from Random Player
# Make AIPlayer inherit from Player and override playMove
# to program AIPlayer using your own algorithm

# class AIPlayer(Player)
class AIPlayer(RandomPlayer):

    def __init__(self, playsFirst : bool):
        super().__init__(playsFirst)

    def playMove(self, game):
        return super().playMove(game)