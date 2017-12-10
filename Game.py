__author__ = 'arsia'

#from Player import *
from TicTacToe.Player import *

class Board:
    def __init__(self):
        self.spots = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def __str__(self):
        result = str(self.spots[0][0]) + " | " + str(self.spots[0][1]) + " | " + str(self.spots[0][2]) + "\n"
        result = result + "---------\n"
        result = result + str(self.spots[1][0]) + " | " + str(self.spots[1][1]) + " | " + str(self.spots[1][2]) + "\n"
        result = result + "---------\n"
        result = result + str(self.spots[2][0]) + " | " + str(self.spots[2][1]) + " | " + str(self.spots[2][2]) + "\n"
        return result

    def is_over(self):

        for i in range(len(self.spots)):
        # check the row match
            if self.spots[i][0] == self.spots[i][1] == self.spots[i][2] != "-":
                print("Player '" + str(self.spots[i][0]).upper() + "' wins on row " + str(i+1))
                return True
        # check the column match
            if self.spots[0][i] == self.spots[1][i] == self.spots[2][i] != "-":
                print("Player '" + str(self.spots[0][i]).upper() + "' wins on col " + str(i+1))
                return True
        # check top left to bottom right diagonal
        if self.spots[0][0] == self.spots[1][1] == self.spots[2][2] != "-":
                print("Player '" + str(self.spots[0][0]).upper() + "' wins on top left to bottom right diagonal")
                return True
        # check top right to bottom left diagonal
        if self.spots[0][2] == self.spots[1][1] == self.spots[2][0] != "-":
                print("Player '" + str(self.spots[0][2]).upper() + "' wins on top right to bottom left diagonal")
                return True
        # if there are empty spots
        for row in range(len(self.spots)):
            for col in range(len(self.spots)):
                if self.spots[row][col] == "-": return False
        # if nothing matches and all spots are marked
        print("No one wins!")
        return True


mygame = Board()
mygame.spots = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
print(mygame)
player_x = CpuPlayer('x')
player_o = Player('o')
endgame = mygame.is_over()
print("Game over? " + str(endgame))

while not endgame:
    player_x.play(mygame)
    print(mygame)
    endgame = mygame.is_over()
    print("Game over? " + str(endgame))
    if not endgame:
        player_o.play(mygame)
        print(mygame)
        endgame = mygame.is_over()
        print("Game over? " + str(endgame))





