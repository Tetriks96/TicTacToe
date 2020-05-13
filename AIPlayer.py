from Player import Player
from typing import List
from Game import *
import math
from random import randrange

def GetSuccessor(gameBoard: List[List[int]], move: int, isMaxPlayer: bool):
    successor = [[0 for col in range(3)] for row in range(3)]
    for row in range(3):
        for col in range(3):
            value = gameBoard[row][col]
            if value == 0:
                if move == 0:
                    successor[row][col] = 1 if isMaxPlayer else -1
                move -= 1
            else:
                successor[row][col] = value
    return successor

def GetSuccessors(gameBoard: List[List[int]], roundNumber: int, isMaxPlayer: bool):
    successors = []
    movesAvailable = 9 - roundNumber
    for move in range(movesAvailable):
        successors.append(GetSuccessor(gameBoard, move, isMaxPlayer))
    return successors

def alphaBeta(gameBoard: List[List[int]], roundNumber: int, depthLimit: int, alpha: int, beta: int, isMaxPlayer: bool):

    outcome = GetOutcome(gameBoard)
    if depthLimit == 0 or outcome != 0:
        return outcome
    
    # Max tries to maximize alpha
    if isMaxPlayer:
        value = -math.inf
        successors = GetSuccessors(gameBoard, roundNumber, isMaxPlayer)

        for successor in successors:
            value = max(value, alphaBeta(successor, roundNumber + 1, depthLimit - 1, alpha, beta, not isMaxPlayer))
            alpha = max(alpha, value)
            if alpha >= beta:
                # Stop. Beta is an upper bound.
                # MinPlayer will not allow any better solution
                break
        return value
    
    # Min tries to minimize beta
    else:
        value = math.inf
        successors = GetSuccessors(gameBoard, roundNumber, isMaxPlayer)

        for successor in successors:
            value = min(value, alphaBeta(successor, roundNumber + 1, depthLimit - 1, alpha, beta, not isMaxPlayer))
            beta = min(beta, value)
            if beta <= alpha:
                # Stop. Alpha is a lower bound
                # MaxPlayer will not allow any better solution
                break
        return value


class AIPlayer(Player):

    def __init__(self, playsFirst: bool):
        self.isMaxPlayer = not playsFirst

    def playMove(self, game: Game):
        bestValue = -1 if self.isMaxPlayer else 1
        successors = GetSuccessors(game.gameBoard, game.roundNumber, self.isMaxPlayer)
        bestSuccessors = []
        for successor in successors:
            value = alphaBeta(successor, game.roundNumber, 9 - game.roundNumber, -1, 1, not self.isMaxPlayer)
            if self.isMaxPlayer and value == 1 or not self.isMaxPlayer and value == -1:
                if bestValue == 0:
                    bestSuccessors = []
                bestValue = value
                bestSuccessors.append(successor)
                break
            elif value == 0:
                if bestValue != 0:
                    bestSuccessors = []
                bestValue = value
                bestSuccessors.append(successor)
        bestSuccessor = bestSuccessors[randrange(len(bestSuccessors))] if len(bestSuccessors) > 0 else successors[randrange(len(successors))]
        for row in range(3):
            for col in range(3):
                if game.gameBoard[row][col] != bestSuccessor[row][col]:
                    super().playMove(game.gameBoard, game.roundNumber, row, col)