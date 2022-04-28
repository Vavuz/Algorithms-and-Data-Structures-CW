'''
Another algorithm
@author Marco Vavassori
@date 28/04/2022
'''

from copy import copy
import random


def generateBoard() -> list:
    '''The algorithm that fills in the grid'''
    fullGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    startIndex = 0
    endIndex = 3
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
            number = random.choice(numbers)
            fullGrid[i][j] = number
            numbers.remove(number)
        
    return fullGrid


def solve(fullGrid) -> bool:
    '''Fills in the rest of the grid'''
    find = findEmpty(fullGrid)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1,10):
        if valid(fullGrid, i, (row, column)):
            fullGrid[row][column] = i

            if solve(fullGrid):
                return True

            fullGrid[row][column] = 0

    return False


def valid(fullGrid, num, position):
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
    blockX = position[1] // 3
    blockY = position[0] // 3
    for i in range(blockY * 3, blockY * 3 + 3):
        for j in range(blockX * 3, blockX * 3 + 3):
            if fullGrid[i][j] == num and (i, j) != position:
                return False

    return True


def printBoard(fullGrid):
    '''Prints the board'''
    for i in range(len(fullGrid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(fullGrid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(fullGrid[i][j])
            else:
                print(str(fullGrid[i][j]) + " ", end="")


def findEmpty(fullGrid):
    '''Finds the first empty cell available'''
    for i in range(len(fullGrid)):
        for j in range(len(fullGrid[0])):
            if fullGrid[i][j] == 0:
                return (i, j)  # row, column
    return None


def removeNumbers(fullGrid):
    '''Removes numbers from the complete grid'''
    counter = 0
    board = fullGrid
    copyBoard = board
    tempCopy = copyBoard

    while True:
        x: int = random.randint(0, 8)
        y: int = random.randint(0, 8)
        if copyBoard[x][y] != 0:
            counter += 1
            copyBoard[x][y] = 0
            tempCopy[x][y] = 0
            printBoard(tempCopy)

            if solve(tempCopy):
                printBoard(copyBoard)
                board = copyBoard
                tempCopy = copyBoard
            else:
                break
            if counter > 5:
                break
    #printBoard(board)



if __name__ == "__main__":
    board = generateBoard()
    solve(board)
    printBoard(board)
    print("\n\n")
    removeNumbers(board)