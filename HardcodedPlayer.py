from Player import Player
from Game import Game
from typing import List

class HardcodedPlayer(Player):

    # For HardcodedPlayer
    # The moves array contains the list of hardcoded moves to play
    # The value of a move determines which empty tile the hardcoded player will fill
    # If the move value is 0, HardcodedPlayer will fill the first empty tile available
    # If the move vaule is 1, HardcodedPlayer will fill the second empty tile available
    # etc...

    # Here are the max valid values for each move number
    # Player 1: [8, 6, 4, 2, 0]
    # Player 2: [7, 5, 3, 1]

    def __init__(self, moves: List[int]):
        self.moves = moves
        self.nextMoveIndex = 0

    def playMove(self, game: Game):
        move = self.moves[self.nextMoveIndex]
        for row in range(3):
            for col in range(3):
                tileValue = game.gameBoard[row][col]
                if tileValue == 0:
                    if move == 0:
                        game.gameBoard[row][col] = -1 if game.roundNumber % 2 == 0 else 1
                        self.nextMoveIndex += 1
                        return
                    move -= 1