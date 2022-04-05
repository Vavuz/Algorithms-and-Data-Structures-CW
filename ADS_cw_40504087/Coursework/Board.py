'''
This file contains the Board class
@author Marco Vavassori
@date 04/02/2022
'''

from Cell import Cell
import math

class Board():
    '''This class manages the game board'''

    def __init__(self, width: int, height: int):
        '''Board class constructor'''
        self.width: int = width
        self.height: int = height
        self.cells: list[Cell] = []
        for i in range(1, (width * height) + 1):
            cell: Cell = Cell(i, 1)
            self.addCell(cell)
        self.coordinates: dict = {'a' : 1,
                                  'A' : 1,
                                  'b' : 2,
                                  'B' : 2,
                                  'c' : 3,
                                  'C' : 3,
                                  'd' : 4,
                                  'D' : 4,
                                  'e' : 5,
                                  'E' : 5,
                                  'f' : 6,
                                  'F' : 6,
                                  'g' : 7,
                                  'G' : 7,
                                  'h' : 8,
                                  'H' : 8,
                                  'i' : 9,
                                  'I' : 9,
                                  'j' : 10,
                                  'J' : 10,
                                  'k' : 11,
                                  'K' : 11,
                                  'l' : 12,
                                  'L' : 12
                                }
    
    def drawBoard(self, choice: int):
        '''Draws the board'''
        #lineLength: int = self.width * 5 + (7 + 5 * choice)
        lineLength: int = self.width * 5 + (choice + 2)
        topBottomLine: str = '-' * lineLength
        internalLine: str = ""
        # The horizontal lines are created
        for i in range(0, lineLength):
            if i == 0 or i == lineLength - 1:
                internalLine += '|'
            elif (i % (6 + 5 * choice)) == 0:
                internalLine += '|'
            else:
                internalLine += '-'
        
        # Board printing
        print("\n" + "\t" + topBottomLine)
        print("\t", end="")
        newEndLineCounter: int = 0
        linesCounter: int = 1
        for cell in self.cells:
            if (newEndLineCounter % math.sqrt(self.width) == 0):
                print("|", end="")
            cell.drawCell()
            newEndLineCounter += 1
            if newEndLineCounter == self.width:
                if (linesCounter % math.sqrt(self.width) == 0 and linesCounter != 0):
                    print("|\n", end="")
                    print("\t", topBottomLine)
                    print("\t", end="")
                else:
                    print("|\n")
                    print("\t", end="")
                newEndLineCounter = 0
                linesCounter += 1
    
    def boardUpdate(self, x: str, y: str, number: int, width: int):
        '''Updates the board'''
        for cell in self.cells:
            if cell.id == (self.coordinates[x] + (width * (int(y) - 1))):
                cell.writeNumber(number)
                break

    def addCell(self, cell: Cell):
        '''Adds a cell to the list of cells'''
        self.cells.append(cell)

    def getWidth(self) -> int:
        '''Returns the width of the board'''
        return self.width

    def getHeight(self) -> int:
        '''Returns the height of the board'''
        return self.height
    
    def getCells(self) -> list[Cell]:
        '''Returns the list of cells'''
        return self.cells