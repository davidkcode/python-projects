
board = [[2, 0, 0, 0, 0, 0, 0, 0, 8],
         [7, 0, 0, 0, 9, 0, 0, 0, 0],
         [6, 0, 5, 0, 3, 0, 0, 0, 0],
         [3, 0, 0, 0, 0, 0, 6, 0, 0],
         [0, 0, 8, 4, 0, 7, 9, 0, 0],
         [1, 0, 0, 6, 8, 0, 0, 0, 0],
         [0, 0, 3, 2, 0, 0, 0, 0, 1],
         [0, 5, 0, 0, 0, 0, 0, 0, 6],
         [0, 0, 0, 8, 0, 0, 0, 4, 0]]


def printBoard():
    # just for styling purposes
    print("\n")

    # Build the grid
    for i in range(0, board.__len__()):
        print(" | ", end=' ')
        for j in range(0, board.__len__()):
            if j % 3 == 0 and j != 0:
                print(" | ", end=' ')
            print(board[i][j], end=' ')
            if j % 8 == 0 and j != 0:
                print(" | ")
        if i == 2 or i == 5:
            print("- - - - - - - - - - - - - - - - -")

    # just for styling purposes
    print("\n")

def solveSudoku():
    solveCell()
    printBoard()

def solveCell():
    # find empty place
    arr = findNextEmpty()
    row = arr[0]
    col = arr[1]
    # This is our goal
    # When no field is empty
    if row == 9:
        return True
    else:
        for i in range(1, 10):
            # Make decisions and check if they are valid
            if isValid(row, col, i):
                # if valid set value to place
                board[row][col] = i
                # search for the next empty place and call solveCell
                if solveCell() == True:
                    return True
                # Undo our decision
                board[row][col] = 0
        return False

def findNextEmpty():
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return [i, j]
    return [9, 9]

def emptyLeft():
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return False
    return True

def isValid(row, col, value):
    #print("isValid function called")
    i = col + 1
    while i <= 8:
        if board[row][i] == value:
            #print("The value is on the same column. On the right side")
            return False
        i += 1

    j = col - 1
    while j >= 0:
        if board[row][j] == value:
            #print("The value is on the same column. On the left side")
            return False
        j -= 1

    k = row + 1
    while k <= 8:
        if board[k][col] == value:
            #print("The value is on the same row. On the bottom side")
            return False
        k += 1

    l = row - 1
    while l >= 0:
        if board[l][col] == value:
            #print("The value is on the same row. On the top side")
            return False
        l -= 1

    if checkSubsquares(row, col, value):
        return False

    return True

def checkSubsquares(row, col, value):
    if row <= 2 and col <= 2:
        for i in range(0, 3):
            for j in range(0, 3):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True
    elif row <= 2 and col > 2 and col <= 5:
        for i in range(0, 3):
            for j in range(3, 6):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True        
    elif row <= 2 and col > 5 and col <= 8:
        for i in range(0, 3):
            for j in range(6, 9):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True
    elif row > 2 and row <= 5 and col <= 2:
        for i in range(3, 6):
            for j in range(0, 3):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True
    elif row > 2 and row <= 5 and col > 2 and col <= 5:
        for i in range(3, 6):
            for j in range(3, 6):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True
    elif row > 2 and row <= 5 and col > 5 and col <= 8:
        for i in range(3, 6):
            for j in range(6, 9):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True
    elif row > 5 and row <= 8 and col <= 2:
        for i in range(6, 9):
            for j in range(0, 3):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True
    elif row > 5 and row <= 8 and col > 2 and col <= 5:
        for i in range(6, 9):
            for j in range(3, 6):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True
    elif row > 5 and row <= 8 and col > 5 and col <= 8:
        for i in range(6, 9):
            for j in range(6, 9):
                if i == row and col == col:
                    continue
                else:
                    if board[i][j] == value:
                        return True

    return False

printBoard()
solveSudoku()
