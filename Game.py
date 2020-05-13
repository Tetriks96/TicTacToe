from Player import Player
from typing import List

def GetOutcome(gameBoard: List[List[int]], filledTiles: int = 9):

    def checkThree(three: List[int]):
        return three[0] if three[0] == three[1] and three[1] == three[2] else 0

    def checkRow(rowIndex: int):
        row = gameBoard[rowIndex]
        return checkThree(row)

    def checkColumn(colIndex: int):
        col = [gameBoard[0][colIndex], gameBoard[1][colIndex], gameBoard[2][colIndex]]
        return checkThree(col)

    def checkDiagonal(diagIndex: int):
        diag = [gameBoard[2 * diagIndex][0], gameBoard[1][1], gameBoard[2 * (1 - diagIndex)][2]]
        return checkThree(diag)

    outcome = 0
    if filledTiles >= 5:
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
    
def printGameboard(gameBoard: List[List[int]]):
    for row in range(3):
        for col in range(3):
            tileValue = gameBoard[row][col]
            tileSymol = ' '
            if tileValue == -1:
                tileSymol = 'X'
            elif tileValue == 1:
                tileSymol = 'O'
            print(tileSymol, end = ' ')
        print()
    print()

class Game:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.roundNumber = 0
        self.gameBoard = [[0 for col in range(3)] for row in range(3)]

    def playRound(self):
        if self.roundNumber < 9:
            player = self.player1 if self.roundNumber % 2 == 0 else self.player2
            player.playMove(self)
            self.roundNumber += 1
            # printGameboard(self.gameBoard)

    def playGame(self):
        outcome = 0
        for i in range(9):
            self.playRound()
            # Note that round number has been incremented by playRound
            outcome = GetOutcome(self.gameBoard, filledTiles = self.roundNumber)
            if outcome != 0:
                break
        return outcome