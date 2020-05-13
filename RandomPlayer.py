from HardcodedPlayer import HardcodedPlayer
from random import randrange as R

class RandomPlayer(HardcodedPlayer):

    def __init__(self, playsFirst: bool):
        moves = [R(9), R(7), R(5), R(3), 0] if playsFirst else [R(8), R(6), R(4), R(2)]
        super().__init__(moves)