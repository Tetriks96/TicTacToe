from Game import Game
from RandomPlayer import RandomPlayer
from AIPlayer import AIPlayer

nRounds = 10

# -1: Player 1 wins
#  0: Draw
#  1: Player 2 wins
#  Note: in python, negative indices wrap back to the end of the array
#  so index = -1 is equivalent to index = 2
outcomes = [0, 0, 0]

for i in range(nRounds):

    player1 = RandomPlayer(playsFirst = True)
    player2 = AIPlayer(playsFirst = False)

    game = Game(player1, player2)
    outcome = game.playGame()

    outcomes[outcome] += 1

    # Control whether or not to print individual round results
    printRounds = True
    if printRounds:
        winner = None
        if outcome == -1:
            winner = 'X'
        elif outcome == 1:
            winner = 'O'
            
        print(f'Winner: {winner}')
        game.printGameboard()

#  Note: in python, negative indices wrap back to the end of the array
#  so index = -1 is equivalent to index = 2
print(f'Number of rounds: {nRounds}')
print(f'Player 1 win rate: {outcomes[-1] / nRounds}')
print(f'Player 2 win rate: {outcomes[1] / nRounds}')
print(f'Draw rate: {outcomes[0] / nRounds}')
print()