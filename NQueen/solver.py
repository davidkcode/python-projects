class NQueenSolver:
    def __init__(self, n):
        self.grid = []

        for i in range(0, n):
            self.grid.append([])
            for j in range(0, n):
                self.grid[i].append(0)

    def solveNQueen(self):
        self.solve(self.grid.__len__(), 0)
        self.printGrid()

    def solve(self, n, row):
        # This is the goal
        # The point when we have placed all queens
        if row == n:
            return True
        else:
            # Iterate through all columns and find a convenient place
            for col in range(0, n):
                # CONTRAINTS
                # check if placement is valid
                if self.isValid(row, col):
                    # set the valid place to 1
                    self.grid[row][col] = 1
                    # call the next function
                    # go to next row
                    if self.solve(n, row + 1) == True:
                        return True
                    # undo our choice
                    self.grid[row][col] = 0
            return False

    def isValid(self, row, col):
        i = row + 1
        j = col + 1
        while i <= 3 and j <= 3:
            if self.grid[i][j] == 1:
                return False
            i += 1
            j += 1

        k = row - 1
        l = col - 1
        while k >= 0 and l >= 0:
            if self.grid[k][l] == 1:
                return False
            k -= 1
            l -= 1

        m = row - 1
        n = col + 1
        while m >= 0 and n <= 3:
            if self.grid[m][n] == 1:
                return False
            m -= 1
            n += 1

        o = row + 1
        p = col - 1
        while o <= 3 and p >= 0:
            if self.grid[o][p] == 1:
                return False
            o += 1
            p -= 1

        r = row + 1
        s = col
        while r <= 3:
            if self.grid[r][s] == 1:
                return False
            r += 1

        t = row - 1
        u = col
        while t >= 0:
            if self.grid[t][u] == 1:
                return False
            t -= 1

        return True

    def printGrid(self):
        print("\n")
        for i in range(0, self.grid.__len__()):
            for j in range(0, self.grid.__len__()):
                print(str(self.grid[i][j]) + " ", end='')
            print("\n")


solver = NQueenSolver(4)
solver.solveNQueen()
