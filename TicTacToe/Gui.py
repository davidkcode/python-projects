import tkinter
from tkinter import Canvas, LEFT, Frame, RIGHT, Button, TOP, Label
from TicTacToe import TicTacToe
from time import sleep

DRAWING_POSITIONS = [[50, 50], [150, 50], [250, 50],
                     [50, 150], [150, 150], [250, 150],
                     [50, 250], [150, 250], [250, 250]]

TEXT_IDS = []


class Gui:
    def __init__(self):
        self.root = tkinter.Tk(className="TicTacToe")
        self.settingsFrame = Frame(self.root, padx=10, pady=10)
        self.gameFrame = Frame(self.root)

        self.gameFrame.pack(side=LEFT, expand=True)
        self.settingsFrame.pack(side=RIGHT, expand=True)

        self.game = TicTacToe()
        self.currentCode = self.game.activePlayer
        self.startPlayer = self.currentCode

        self.canvas = Canvas(self.gameFrame, width=300, height=300)
        self.drawGrid()
        self.createSettingsFrame()

        self.canvas.bind('<Button-1>', self.clickHandler)
        self.root.mainloop()

    def clickHandler(self, event):
        x, y = event.x, event.y

        if x < 100 and y < 100:
            self.drawCode(self.currentCode, 0)
        elif x > 100 and x < 200 and y < 100:
            self.drawCode(self.currentCode, 1)
        elif x > 200 and x < 300 and y < 100:
            self.drawCode(self.currentCode, 2)
        elif x < 100 and y > 100 and y < 200:
            self.drawCode(self.currentCode, 3)
        elif x > 100 and x < 200 and y > 100 and y < 200:
            self.drawCode(self.currentCode, 4)
        elif x > 200 and x < 300 and y > 100 and y < 200:
            self.drawCode(self.currentCode, 5)
        elif x < 100 and y > 200 and y < 300:
            self.drawCode(self.currentCode, 6)
        elif x > 100 and x < 200 and y > 200 and y < 300:
            self.drawCode(self.currentCode, 7)
        elif x > 200 and x < 300 and y > 200 and y < 300:
            self.drawCode(self.currentCode, 8)

    def createSettingsFrame(self):
        Label(self.settingsFrame, text="Score",
              font="Arial 15", pady=15).pack(side=TOP)
        Label(self.settingsFrame, text="Player1",
              font="Arial 10").pack(side=TOP)
        Label(self.settingsFrame, textvariable=self.game.winsPlayerOne,
              font="Arial 8").pack(side=TOP)
        Label(self.settingsFrame, text="Player2",
              font="Arial 10").pack(side=TOP)
        Label(self.settingsFrame, textvariable=self.game.winsPlayerTwo,
              font="Arial 8").pack(side=TOP)

    def drawGrid(self):
        self.canvas.create_line(0, 100, 400, 100)
        self.canvas.create_line(0, 200, 400, 200)
        self.canvas.create_line(100, 0, 100, 300)
        self.canvas.create_line(200, 0, 200, 300)
        self.canvas.create_line(300, 0, 300, 300)
        self.canvas.pack()

    def deleteAll(self):
        for ele in TEXT_IDS:
            self.canvas.delete(ele)
        self.game.resetGrid()
        self.canvas.bind('<Button-1>', self.clickHandler)

    def drawCode(self, code, pos):
        arr = DRAWING_POSITIONS[pos]

        if self.game.checkMoveIfValid(pos, code):
            TEXT_IDS.append(self.canvas.create_text(
                arr[0], arr[1], text=self.currentCode, font="Arial 40"))
            row = self.game.checkWin(self.currentCode)
            remis = self.game.checkRemis()
            if remis:
                self.canvas.unbind('<Button-1>')
                self.gameFrame.after(2000, self.deleteAll)
            if row:
                if row == 1:
                    TEXT_IDS.append(self.canvas.create_line(25, 50, 275, 50))
                elif row == 2:
                    TEXT_IDS.append(self.canvas.create_line(25, 150, 275, 150))
                elif row == 3:
                    TEXT_IDS.append(self.canvas.create_line(25, 250, 275, 250))
                elif row == 4:
                    TEXT_IDS.append(self.canvas.create_line(50, 25, 50, 275))
                elif row == 5:
                    TEXT_IDS.append(self.canvas.create_line(150, 25, 150, 275))
                elif row == 6:
                    TEXT_IDS.append(self.canvas.create_line(250, 25, 250, 275))
                elif row == 7:
                    TEXT_IDS.append(self.canvas.create_line(25, 25, 275, 275))
                elif row == 8:
                    TEXT_IDS.append(self.canvas.create_line(25, 275, 275, 25))
                self.canvas.unbind('<Button-1>')
                self.gameFrame.after(2000, self.deleteAll)
            self.game.switchPlayer()
            self.currentCode = self.game.activePlayer


if __name__ == "__main__":
    Gui()
