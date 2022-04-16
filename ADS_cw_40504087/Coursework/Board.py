'''
This file contains the Board class
@author Marco Vavassori
@date 04/02/2022
'''

from Cell import Cell
from colorama import Fore, init
from termcolor import colored
import math
import random


class Board():
    '''This class manages the game board'''

    def __init__(self, width: int, height: int):
        '''Board class constructor'''
        self.width: int = width
        self.height: int = height
        self.cells: list[Cell] = []
        #self.color = random.choice(dict(Fore.__dict__.items()).keys())
        init(autoreset=True)
        for i in range(0, (width * height)):
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
                                }
    
    def drawBoard(self, choice: int):
        '''Draws the board'''
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
        horizontalCoords: str = ""
        horizontalCoordsCounter: int = 0
        keysList = list(self.coordinates.keys())
        # The horizontal coordinates are written from the dictionary of coordinates
        for i in range(1, self.width * 2, 2):
            horizontalCoordsCounter += 1
            horizontalCoords += keysList[i]
            if horizontalCoordsCounter == math.sqrt(self.width):
                horizontalCoords += "     "
                horizontalCoordsCounter = 0
            else:
                horizontalCoords += "    "
        print("\n\t     " + colored(horizontalCoords, 'yellow'))

        print("\t  " + Fore.MAGENTA + topBottomLine)
        print("\t", end="")
        newEndLineCounter: int = 0
        linesCounter: int = 1
        verticalCoordsCounter: int = math.sqrt(self.width)
        verticalCoords: int = 1
        # Every cell needs to be printed
        for cell in self.cells:
            if (newEndLineCounter % math.sqrt(self.width) == 0):
                # When we get to a new  line
                if verticalCoordsCounter == math.sqrt(self.width):
                    print(colored(str(verticalCoords), 'yellow') + " " + Fore.MAGENTA + "|", end="")
                    verticalCoordsCounter = 1
                    verticalCoords += 1
                # When we are in the middle of the line
                else:
                    print(Fore.MAGENTA + "|", end="")
                    verticalCoordsCounter += 1
            cell.drawCell()    # cell printing
            newEndLineCounter += 1
            # Divider lines printing
            if newEndLineCounter == self.width:
                if (linesCounter % math.sqrt(self.width) == 0 and linesCounter != 0 and linesCounter != self.height):
                    print(Fore.MAGENTA + "|\n", end="")
                    print("\t  " + Fore.MAGENTA + internalLine)
                    print("\t", end="")
                elif (linesCounter == self.height):
                    print(Fore.MAGENTA + "|\n", end="")
                    print("\t  " + Fore.MAGENTA + topBottomLine)
                else:
                    print(Fore.MAGENTA + "|\n")
                    print("\t", end="")
                newEndLineCounter = 0
                linesCounter += 1
    
    def boardUpdate(self, x: str, y: str, number: int, width: int):
        '''Updates the board'''
        for cell in self.cells:
            if cell.id == (self.coordinates[x] + (width * (int(y) - 1)) - 1):
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