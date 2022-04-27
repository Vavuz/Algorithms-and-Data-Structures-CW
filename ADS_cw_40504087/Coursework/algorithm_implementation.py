'''
Algorithm implementation
@author Marco Vavassori
@date 27/04/2022
'''


import random


def algorithmStarted(size: int):
    '''The algorithm that fills in the grid'''
    fullGrid = [0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Blocks
    firstBlock: list = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    secondBlock: list = [3, 4, 5, 12, 13, 14, 21, 22, 23]
    thirdBlock: list = [6, 7, 8, 15, 16, 17, 24, 25, 26]
    fourthBlock: list = [27, 28, 29, 36, 37, 38, 45, 46, 47]
    fifthBlock: list = [30, 31, 32, 39, 40, 41, 48, 49, 50]
    sixthBlock: list = [33, 34, 35, 42, 43, 44, 51, 52, 53]
    seventhBlock: list = [54, 55, 56, 63, 64, 65, 72, 73, 74]
    eighthBlock: list = [57, 58, 59, 66, 67, 68, 75, 76, 77]
    ninthtBlock: list = [60, 61, 62, 69, 70, 71, 78, 79, 80]

    # The loop will act over every block in the grid, for 'size' times
    for i in range (0, size):
        if (i == 0 or i == 1):
            # One
            numChoice = random.choice(firstBlock)
            fullGrid[numChoice] = 1
            # Two
            numChoice = random.choice(secondBlock)
            fullGrid[numChoice] = 1
            # Three
            # Four
            # Five
            # Six
            # Seven
            # Eight
            # Nine
        else:
            # One
            # Two
            # Three
            # Four
            # Five
            # Six
            # Seven
            # Eight
            # Nine
            pass
    pass    

def one():
    pass

def findRow(index: int) -> int:
    '''Finds the row of a cell'''
    row = 1
    
    # Rows
    firstRow: list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    secondRow: list = [9, 10, 11, 12, 13, 14, 15, 16, 17]
    thirdRow: list = [18, 19, 20, 21, 22, 23, 24, 25, 26]
    fourthRow: list = [27, 28, 29, 30, 31, 32, 33, 34, 35]
    fifthRow: list = [36, 37, 38, 39, 40, 41, 42, 43, 44]
    sixthRow: list = [45, 46, 47, 48, 49, 50, 51, 52, 53]
    seventhRow: list = [54, 55, 56, 57, 58, 59, 60, 61, 62]
    eighthRow: list = [63, 64, 65, 66, 67, 68, 69, 70, 71]
    ninthtRow: list = [72, 73, 74, 75, 76, 77, 78, 79, 80]

    # find row
    if (secondRow.count(index) > 0):
        row = 2
    elif (thirdRow.count(index) > 0):
        row = 3
    elif (fifthRow.count(index) > 0):
        row = 2
    elif (sixthRow.count(index) > 0):
        row = 3
    elif (eighthRow.count(index) > 0):
        row = 2
    elif (ninthtRow.count(index) > 0):
        row = 3
    else:
        pass

    return row

def findColumn(index: int) -> int:
    '''Finds the column of a cell'''
    column = 1

    # Columns
    firstColumn: list = [0, 9, 18, 27, 36, 45, 54, 63, 72]
    secondColumn: list = [1, 10, 19, 28, 37, 46, 55, 64, 73]
    thirdColumn: list = [2, 11, 20, 29, 38, 47, 56, 65, 74]
    fourthColumn: list = [3, 12, 21, 30, 39, 48, 57, 66, 75]
    fifthColumn: list = [4, 13, 22, 31, 40, 49, 58, 67, 76]
    sixthColumn: list = [5, 14, 23, 32, 41, 50, 59, 68, 77]
    seventhColumn: list = [6, 15, 24, 33, 42, 51, 60, 69, 78]
    eighthColumn: list = [7, 16, 25, 34, 43, 52, 61, 70, 79]
    ninthtColumn: list = [8, 17, 26, 35, 44, 53, 62, 71, 80]
    
    # find row
    if (secondColumn.count(index) > 0):
        column = 2
    elif (thirdColumn.count(index) > 0):
        column = 3
    elif (fifthColumn.count(index) > 0):
        column = 2
    elif (sixthColumn.count(index) > 0):
        column = 3
    elif (eighthColumn.count(index) > 0):
        column = 2
    elif (ninthtColumn.count(index) > 0):
        column = 3
    else:
        pass

    return column

        

if __name__ == "__main__":
    algorithmStarted(9)
    input()