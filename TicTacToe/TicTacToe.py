from tkinter import StringVar
from time import sleep


class TicTacToe:
    def __init__(self):
        self.playerOneCode = "X"  # X
        self.playerTwoCode = "O"  # O

        self.winsPlayerOne = StringVar()
        self.winsPlayerTwo = StringVar()

        self.winsPlayerOne.set("0")
        self.winsPlayerTwo.set("0")

        self.activePlayer = self.playerOneCode
        self.gridSystem = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0]

    def switchPlayer(self):
        if self.activePlayer == self.playerOneCode:
            self.activePlayer = self.playerTwoCode
        elif self.activePlayer == self.playerTwoCode:
            self.activePlayer = self.playerOneCode

    def checkWin(self, code):
        if self.gridSystem[0] == code and self.gridSystem[1] == code and self.gridSystem[2] == code:
            self.setWins(code)
            return 1  # horizontal von links
        elif self.gridSystem[3] == code and self.gridSystem[4] == code and self.gridSystem[5] == code:
            self.setWins(code)
            return 2
        elif self.gridSystem[6] == code and self.gridSystem[7] == code and self.gridSystem[8] == code:
            self.setWins(code)
            return 3
        elif self.gridSystem[0] == code and self.gridSystem[3] == code and self.gridSystem[6] == code:
            self.setWins(code)
            return 4  # vertikal von links
        elif self.gridSystem[1] == code and self.gridSystem[4] == code and self.gridSystem[7] == code:
            self.setWins(code)
            return 5
        elif self.gridSystem[2] == code and self.gridSystem[5] == code and self.gridSystem[8] == code:
            self.setWins(code)
            return 6
        elif self.gridSystem[0] == code and self.gridSystem[4] == code and self.gridSystem[8] == code:
            self.setWins(code)
            return 7  # diagonal von links beginnend
        elif self.gridSystem[2] == code and self.gridSystem[4] == code and self.gridSystem[6] == code:
            self.setWins(code)
            return 8  # diagonal von rechts beginnend
        else:
            return False

    def checkRemis(self):
        for ele in self.gridSystem:
            if ele == 0:
                return False
        return True

    def setWins(self, code):
        if code == "X":
            self.winsPlayerOne.set(str(int(self.winsPlayerOne.get()) + 1))
        elif code == "O":
            self.winsPlayerTwo.set(str(int(self.winsPlayerTwo.get()) + 1))

    def checkMoveIfValid(self, pos, code):
        if self.gridSystem[pos] == 0:
            self.gridSystem[pos] = code
            return True
        else:
            return False

    def resetGrid(self):
        self.gridSystem = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0]
