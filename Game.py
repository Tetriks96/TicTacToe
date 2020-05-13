from Player import Player
from typing import List

class Game:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.roundNumber = 0
        self.gameBoard = [[0 for col in range(3)] for row in range(3)]

    def getOutcome(self):

        def checkThree(three: List[int]):
            return three[0] if three[0] == three[1] and three[1] == three[2] else 0

        def checkRow(rowIndex: int):
            row = self.gameBoard[rowIndex]
            return checkThree(row)

        def checkColumn(colIndex: int):
            col = [self.gameBoard[0][colIndex], self.gameBoard[1][colIndex], self.gameBoard[2][colIndex]]
            return checkThree(col)

        def checkDiagonal(diagIndex: int):
            diag = [self.gameBoard[2 * diagIndex][0], self.gameBoard[1][1], self.gameBoard[2 * (1 - diagIndex)][2]]
            return checkThree(diag)

        outcome = 0
        for i in range(3):
            outcome += checkColumn(i)
            outcome += checkRow(i)

        outcome += checkDiagonal(0)
        outcome += checkDiagonal(1)

        if outcome < 0:
            return -1
        elif outcome > 0:
            return 1
        else:
            return 0

    def playRound(self):
        if self.roundNumber < 9:
            player = self.player1 if self.roundNumber % 2 == 0 else self.player2
            player.playMove(self)
            self.roundNumber += 1

    def playGame(self):
        outcome = 0
        for i in range(9):
            self.playRound()
            filledTiles = self.roundNumber + 1
            if filledTiles >= 5:
                outcome = self.getOutcome()
                if outcome != 0:
                    break

        return outcome
    
    def printGameboard(self):
        for row in range(3):
            for col in range(3):
                tileValue = self.gameBoard[row][col]
                tileSymol = ' '
                if tileValue == -1:
                    tileSymol = 'X'
                elif tileValue == 1:
                    tileSymol = 'O'
                print(tileSymol, end = ' ')
            print()
        print()
