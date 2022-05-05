'''
This file contains the GridGenerator class
@author Marco Vavassori
'''

import copy
import random



class GridGenerator():
    '''This class generates the numbers that are going to be put in the sudoku grid'''

    def __init__(self, size: int, choice: int):
        '''GridGenerator class constructor'''
        self.size = size
        self.choice = choice
        self.gridWithClues: list[int] = self.generateBoardWithClues()


    def getGrid(self) -> list[int]:
        '''Returns the grid'''
        return self.gridWithClues


    def generateBoardWithClues(self) -> list[int]:
        '''Converts the grid from a 2d array to a 1d array'''
        if self.size == 9:
            # 9x9 grid is generated, solved and partially emptied
            grid: list[list[int]] = self.generateBigPartialBoard()
            self.solveBig(grid)
            grid = self.removeNumbersBig(grid)
        else:
            # 4x4 grid is generated, solved and partially emptied
            while True:
                grid: list[list[int]] = self.generateSmallPartialBoard()
                self.solveSmall(grid)
                zeros: bool = False
                for row in grid:
                    for n in row:
                        if n == 0:
                            zeros = True
                            break
                if not zeros:
                    break
            grid = self.removeNumbersSmall(grid)

        # Converts 2d array into 1d array
        newGrid: list[int] = []
        for row in grid:
            for n in row:
                newGrid.append(n)
        return newGrid


    def generateBigPartialBoard(self) -> list[list[int]]:
        '''The algorithm that fills in the diagonal blocks of the grid'''
        fullGrid: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        startIndex: int = 0
        endIndex: int = 3

        # The diagonal blocks are filled in
        for i in range(9):
            if i % 3 == 0:
                numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            if (i > 5):
                startIndex = 6
                endIndex = 9
            elif (i > 2):
                startIndex = 3
                endIndex = 6
            else:
                pass

            for j in range(startIndex, endIndex):
                number: int = random.choice(numbers)
                fullGrid[i][j] = number
                numbers.remove(number)
            
        return fullGrid


    def generateSmallPartialBoard(self) -> list[list[int]]:
        '''The algorithm that fills in the grid'''
        fullGrid: list[list[int]] = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

        numbers: list[int] = [1, 2, 3, 4]
        startIndex: int = 0
        endIndex: int = 2
        
        # The diagonal blocks are filled in
        for i in range(4):
            if i % 2 == 0:
                numbers = [1, 2, 3, 4]
            if (i > 1):
                startIndex = 2
                endIndex = 4
            else:
                pass

            for j in range(startIndex, endIndex):
                number: int = random.choice(numbers)
                fullGrid[i][j] = number
                numbers.remove(number)
        return fullGrid


    def solveBig(self, fullGrid: list[list[int]]) -> bool:
        '''Fills in the rest of the 9x9 grid'''
        find: tuple[int, int] | None = self.findEmpty(fullGrid)
        if find == None:
            return True
        else:
            row: int = find[0]
            column: int = find[1]

        # Trying out every number from 1 to 9 with backtracking
        for i in range(1, 10):
            if self.valid(fullGrid, i, (row, column)):
                fullGrid[row][column] = i

                if self.solveBig(fullGrid):
                    return True

                fullGrid[row][column] = 0

        return False


    def solveSmall(self, fullGrid: list[list[int]]) -> bool:
        '''Fills in the rest of the 4x4 grid'''
        find: tuple[int, int] | None = self.findEmpty(fullGrid)
        if find == None:
            return True
        else:
            row: int = find[0]
            column: int = find[1]

        # Trying out every number from 1 to 4 with backtracking
        for i in range(1, 5):
            if self.valid(fullGrid, i, (row, column)):
                fullGrid[row][column] = i

                if self.solveSmall(fullGrid):
                    return True

                fullGrid[row][column] = 0

        return False


    def valid(self, fullGrid: list[list[int]], num: int, position: int) -> bool:
        '''Checks that the number can be inserted without interference'''
        # Check row
        for i in range(len(fullGrid[0])):
            if fullGrid[position[0]][i] == num and position[1] != i:
                return False

        # Check column
        for i in range(len(fullGrid)):
            if fullGrid[i][position[1]] == num and position[0] != i:
                return False

        # Check block
        if len(fullGrid) == 9:
            blockX: int = position[1] // 3
            blockY: int = position[0] // 3
            for i in range(blockY * 3, blockY * 3 + 3):
                for j in range(blockX * 3, blockX * 3 + 3):
                    if fullGrid[i][j] == num and (i, j) != position:
                        return False
        else:
            blockX: int = position[1] // 2
            blockY: int = position[0] // 2
            for i in range(blockY * 2, blockY * 2 + 2):
                for j in range(blockX * 2, blockX * 2 + 2):
                    if fullGrid[i][j] == num and (i, j) != position:
                        return False

        return True


    def findEmpty(self, fullGrid: list[list[int]]) -> tuple[int, int] | None:
        '''Finds the first empty cell available'''
        for i in range(len(fullGrid)):
            for j in range(len(fullGrid[0])):
                if fullGrid[i][j] == 0:
                    return (i, j)  # row, column
        return None


    def removeNumbersBig(self, fullGrid: list[list[int]]) -> list[list[int]]:
        '''Removes numbers from the 9x9 complete grid'''
        counter: int = 56
        board: list = copy.deepcopy(fullGrid)
        copyBoard: list = copy.deepcopy(fullGrid)
        tempCopy: list = copy.deepcopy(fullGrid)

        # Removing numbers according to the difficulty level chosen
        if self.choice == 1:
            counter = 36
        elif self.choice == 2:
            counter = 46

        # Removing and checking if solvable with backtracking
        while True:
            x: int = random.randint(0, 8)
            y: int = random.randint(0, 8)
            if copyBoard[x][y] != 0:
                copyBoard[x][y] = 0
                tempCopy[x][y] = 0

                if self.solveBig(tempCopy):
                    counter -= 1
                    board = copy.deepcopy(copyBoard)
                    tempCopy = copy.deepcopy(copyBoard)
                else:
                    break

                if counter == 0:
                    break
        return board


    def removeNumbersSmall(self, fullGrid: list[list[int]]) -> list[list[int]]:
        '''Removes numbers from the 4x4 complete grid'''
        counter: int = 0
        board: list = copy.deepcopy(fullGrid)
        copyBoard: list = copy.deepcopy(fullGrid)
        tempCopy: list = copy.deepcopy(fullGrid)

        # Removing and checking if solvable with backtracking
        while True:
            x: int = random.randint(0, 3)
            y: int = random.randint(0, 3)
            if copyBoard[x][y] != 0:
                copyBoard[x][y] = 0
                tempCopy[x][y] = 0

                if self.solveSmall(tempCopy):
                    counter += 1
                    board = copy.deepcopy(copyBoard)
                    tempCopy = copy.deepcopy(copyBoard)
                else:
                    break
                if counter == 11:
                    break

        return board