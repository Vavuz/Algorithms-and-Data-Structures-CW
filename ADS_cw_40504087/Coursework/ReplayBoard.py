'''
This file contains the Board class
@author Marco Vavassori
'''

from Cell import Cell
from GridGenerator import GridGenerator
from colorama import Fore, init
from termcolor import colored
import math


class ReplayBoard():
    '''This class manages the game board'''

    def __init__(self, size: int, allCellsStatusAndContent: list[list[bool], list[int]]):
        '''Board class constructor'''
        self.size: int = size
        self.cells: list[Cell] = []
        init(autoreset=True)
        self.allCellsStatusAndContent: list[list[bool], list[int]] = allCellsStatusAndContent

        for i in range(0, (size ** 2)):
            cell: Cell = Cell(i, allCellsStatusAndContent[0][i], allCellsStatusAndContent[1][i])
            self.cells.append(cell)

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
        lineLength: int = self.size * 5 + (choice + 2)
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

        # Horizontal coordinates printing
        horizontalCoords: str = ""
        horizontalCoordsCounter: int = 0
        keysList = list(self.coordinates.keys())
        # The horizontal coordinates are written from the dictionary of coordinates
        for i in range(1, self.size * 2, 2):
            horizontalCoordsCounter += 1
            horizontalCoords += keysList[i]
            if horizontalCoordsCounter == math.sqrt(self.size):
                horizontalCoords += "     "
                horizontalCoordsCounter = 0
            else:
                horizontalCoords += "    "      
        print("\n\t     " + colored(horizontalCoords, 'yellow'), end="")
        
        # Board printing
        print("\t  " + Fore.MAGENTA + topBottomLine)
        print("\t", end="")
        newEndLineCounter: int = 0
        linesCounter: int = 1
        verticalCoordsCounter: int = math.sqrt(self.size)
        verticalCoords: int = 1
        # Every cell needs to be printed
        for cell in self.cells:
            if (newEndLineCounter % math.sqrt(self.size) == 0):
                # When we get to a new  line
                if verticalCoordsCounter == math.sqrt(self.size):
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
            if newEndLineCounter == self.size:
                if (linesCounter % math.sqrt(self.size) == 0 and linesCounter != 0 and linesCounter != self.size):
                    print(Fore.MAGENTA + "|\n", end="")
                    print("\t  " + Fore.MAGENTA + internalLine)
                    print("\t", end="")
                elif (linesCounter == self.size):
                    print(Fore.MAGENTA + "|\n", end="")
                    print("\t  " + Fore.MAGENTA + topBottomLine)
                else:
                    print(Fore.MAGENTA + "|\n")
                    print("\t", end="")
                newEndLineCounter = 0
                linesCounter += 1
        
        spacing: int = 3 if self.size == 9 else 5
        totLeft: int = 0
        for cell in self.cells:
            if cell.currentNumber == 0:
                totLeft += 1
        print("\t     " + " " * self.size * 5 + "\t" * spacing + "Completed: " + Fore.CYAN + str(len(self.cells) - totLeft) + " / " +  str(len(self.cells)))

    
    def boardUpdate(self, x: str, y: str, number: int, size: int):
        '''Updates the board'''
        for cell in self.cells:
            if cell.id == (self.coordinates[x] + (size * (int(y) - 1)) - 1):
                cell.writeNumber(number)
                break