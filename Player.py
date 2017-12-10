__author__ = 'arsia'

class CpuPlayer:

    def __init__(self, mark):
        self.mark = mark
        self.round = 1       # To track if it is the first or second or ... move by computer
        self.op = '-'        # What marker the opponent is using (x or o)?
        self.moved = False   # To make sure we do not mark more than one spot in each round
        if self.mark == 'x':
            self.op = 'o'
        else:
            self.op = 'x'

    def play(self, board):
        # First move by computer
        if self.round == 1:
            if board.spots[0][0] == '-':
                board.spots[0][0] = self.mark
            self.round += 1

        # Second move by computer
        elif self.round == 2:
            if (board.spots[0][1] == self.op or board.spots[1][0] == self.op or
                board.spots[1][2] == self.op or board.spots[2][1] == self.op)and board.spots[1][1] == '-':
                board.spots[1][1] = self.mark
            elif (board.spots[2][0] == self.op or board.spots[2][2] == self.op) and board.spots[0][2] == '-':
                board.spots[0][2] = self.mark
            elif board.spots[0][2] == self.op and board.spots[2][0] == '-':
                board.spots[2][0] = self.mark
            elif board.spots[1][1] == self.op and board.spots[2][2] == '-':
                board.spots[2][2] = self.mark
            self.round += 1

        # Third move by computer
        elif self.round == 3:
            self.moved = False
            if not self.moved:
                # check for 2 self.mark in any row and mark the third spot if empty
                if self.checkRowCol(board,self.mark):
                    self.moved = True
                elif self.checkDiagonals(board,self.mark):
                    self.moved = True
                elif self.checkRowCol(board,self.op):
                    self.moved = True
                elif self.checkDiagonals(board,self.op):
                    self.moved = True

            if not self.moved:
                # check for following case
                #  x | o | -
                #  ---------
                #  - | x | -
                #  ---------
                #  X | - | o
                if board.spots[0][0] == board.spots[1][1] == self.mark and \
                    board.spots[0][1] == board.spots[2][2] == self.op and board.spots[2][0] == "-":
                    board.spots[2][0] = self.mark
                    self.moved = True

                # check for following case
                #  x | - | o
                #  ---------
                #  o | - | -
                #  ---------
                #  x | - | X
                elif board.spots[0][0] == board.spots[2][0] == self.mark and \
                    board.spots[1][0] == board.spots[0][2] == self.op and board.spots[2][2] == "-":
                    board.spots[2][2] = self.mark
                    self.moved = True

                # check for following case
                #  x | - | X
                #  ---------
                #  o | x | -
                #  ---------
                #  - | - | o
                elif board.spots[0][0] == board.spots[1][1] == self.mark and \
                    board.spots[1][0] == board.spots[2][2] == self.op and board.spots[0][2] == "-":
                    board.spots[0][2] = self.mark
                    self.moved = True

                # check for following case
                #  x | o | x
                #  ---------
                #  - | - | -
                #  ---------
                #  o | - | X
                elif board.spots[0][0] == board.spots[0][2] == self.mark and \
                    board.spots[0][1] == board.spots[2][0] == self.op and board.spots[2][2] == "-":
                    board.spots[2][2] = self.mark
                    self.moved = True

                # check for following case
                #  x | o | x
                #  ---------
                #  - | - | -
                #  ---------
                #  X | - | o
                elif board.spots[0][0] == board.spots[0][2] == self.mark and \
                    board.spots[0][1] == board.spots[2][2] == self.op and board.spots[2][0] == "-":
                    board.spots[2][0] = self.mark
                    self.moved = True

            self.round += 1

        # Forth move by computer
        elif self.round == 4:
            self.moved = False
            # check for 2 self.mark in any row and mark the third spot if empty
            if self.checkRowCol(board,self.mark):
                self.moved = True
            elif self.checkDiagonals(board,self.mark):
                self.moved = True
            elif self.checkRowCol(board,self.op):
                self.moved = True
            elif self.checkDiagonals(board,self.op):
                self.moved = True

            self.round += 1

        # Fifth move by computer
        elif self.round == 5:
            self.moved = False
            # check for 2 self.mark in any row and mark the third spot if empty
            if self.checkRowCol(board,self.mark):
                self.moved = True
            elif self.checkDiagonals(board,self.mark):
                self.moved = True
            elif self.checkRowCol(board,self.op):
                self.moved = True
            elif self.checkDiagonals(board,self.op):
                self.moved = True

#######################################################################################################################

    def checkRowCol(self, board, mrk):
        for i in range(len(board.spots)):
            # check for 2 mrk in any row and mark the third spot if empty
            if board.spots[i][0] == board.spots[i][1] == str(mrk) and board.spots[i][2] == '-':
                board.spots[i][2] = self.mark
                return True
            elif board.spots[i][0] == board.spots[i][2] == str(mrk) and board.spots[i][1] == '-':
                board.spots[i][1] = self.mark
                return True
            elif board.spots[i][1] == board.spots[i][2] == str(mrk) and board.spots[i][0] == '-':
                board.spots[i][0] = self.mark
                return True
            # check for 2 mrk in any col and mark the third spot if empty
            elif board.spots[0][i] == board.spots[1][i] == str(mrk) and board.spots[2][i] == '-':
                board.spots[2][i] = self.mark
                return True
            elif board.spots[0][i] == board.spots[2][i] == str(mrk) and board.spots[1][i] == '-':
                board.spots[1][i] = self.mark
                return True
            elif board.spots[1][i] == board.spots[2][i] == str(mrk) and board.spots[0][i] == '-':
                board.spots[0][i] = self.mark
                return True

        return False

#######################################################################################################################

    def checkDiagonals(self, board, mrk):
        # check for 2 mrk in top left to bottom right diagonal and mark the third spot if empty
        if (board.spots[0][0] == board.spots[1][1] == mrk) and board.spots[2][2] == '-':
            board.spots[2][2] = self.mark
            return True
        elif (board.spots[0][0] == board.spots[2][2] == mrk) and board.spots[1][1] == '-':
            board.spots[1][1] = self.mark
            return True
        elif (board.spots[1][1] == board.spots[2][2] == mrk) and board.spots[0][0] == '-':
            board.spots[0][0] = self.mark
            return True
        # check for 2 mrk in top right to bottom left diagonal and mark the third spot if empty
        elif (board.spots[0][2] == board.spots[1][1] == mrk) and board.spots[2][0] == "-":
            board.spots[2][0] = self.mark
            return True
        elif (board.spots[0][2] == board.spots[2][0] == mrk) and board.spots[1][1] == "-":
            board.spots[1][1] = self.mark
            return True
        elif (board.spots[1][1] == board.spots[2][0] == mrk) and board.spots[0][2] == "-":
            board.spots[0][2] = self.mark
            return True

        return False

#######################################################################################################################

class Player:
    def __init__(self, mark):
        self.mark = mark

    def play(self, board):
        spot = input("Where do you want to play? ")
        while len(spot) < 2:
            spot = input("Bad input, try again: ")
        row = int(spot[0])
        col = int(spot[1])
        while board.spots[row][col] != "-":
            print ("The spot " + spot + " is not empty! choose another spot.")
            spot = input("Where do you want to play? ")
            row = int(spot[0])
            col = int(spot[1])

        if board.spots[row][col] == "-":
            board.spots[row][col] = self.mark




