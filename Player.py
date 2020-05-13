from typing import List

class Player:

    def playMove(self, gameBoard: List[List[int]], roundNumber, row, col):
        gameBoard[row][col] = -1 if roundNumber % 2 == 0 else 1