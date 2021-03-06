'''
This file contains the Board class
@author Marco Vavassori
'''

from Cell import Cell
from GridGenerator import GridGenerator
from colorama import Fore, init
from termcolor import colored
import math



class Board():
    '''This class manages the game board'''

    def __init__(self, width: int, height: int, choice: int):
        '''Board class constructor'''
        self.width: int = width
        self.height: int = height
        self.choice: int = choice
        self.cells: list[Cell] = []    # stores the cells
        init(autoreset=True)
        self.allCellsStatusAndContent: list[list[bool], list[int]] = self.generateRiddle()    # stores the predefined cells

        # Cells generation
        for i in range(0, (width * height)):
            cell: Cell = Cell(i, self.allCellsStatusAndContent[0][i], self.allCellsStatusAndContent[1][i])
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
                                }             # Dictionary of the coordinates
    
    
    def drawBoard(self, choice: int, sudokuTimer: int):
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

        # Horizontal coordinates printing
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
        print("\n\t     " + colored(horizontalCoords, 'yellow'), end="")

        # Print timer
        seconds: str = str(sudokuTimer % 60)
        if (int(seconds) < 10):
            seconds = '0' + seconds
        timeLeft: str = str(round(sudokuTimer // 60)) + ':' + str(seconds)
        spacing: int = 3 if self.width == 9 else 5
        if (sudokuTimer > 240):
            print("\t" * spacing + "Time left: " + colored(timeLeft, 'green'))
        elif (sudokuTimer > 60):
            print("\t" * spacing + "Time left: " + colored(timeLeft, 'yellow'))
        else:
            print("\t" * spacing + "Time left: " + colored(timeLeft, 'red'))
        
        # Board printing
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
        
        # Total cells remaining printing
        totLeft: int = 0
        for cell in self.cells:
            if cell.currentNumber == 0:
                totLeft += 1
        print("\t     " + " " * self.width * 5 + "\t" * spacing + "Completed: " + Fore.CYAN + str(len(self.cells) - totLeft) + " / " +  str(len(self.cells)))
    

    def generateRiddle(self) -> list[list[bool], list[int]]:
        '''Generates all the pre-written numbers in the sudoku table'''
        gridGenerator: GridGenerator = GridGenerator(self.width, self.choice)    # the GridGenerator object will handle the algorithms
        grid: list[int] = gridGenerator.getGrid()    # the grid with the clues

        # AllCellsStatusAndContent is filled
        allCellsStatusAndContent: list[list[bool], list[int]] = [[], []]
        for number in grid:
            if number != 0:
                allCellsStatusAndContent[0].append(False)
            else:
                allCellsStatusAndContent[0].append(True)
            allCellsStatusAndContent[1].append(number)

        return allCellsStatusAndContent

    
    def boardUpdate(self, x: str, y: str, number: int, width: int):
        '''Updates the board'''
        for cell in self.cells:
            if cell.id == (self.coordinates[x] + (width * (int(y) - 1)) - 1):
                cell.writeNumber(number)
                break
    
    
    def isFull(self):
        '''Returns true if the sudoku has been completed'''
        for cell in self.cells:
            if cell.currentNumber == 0:
                return False
        return True


    def addCell(self, cell: Cell):
        '''Adds a cell to the list of cells'''
        self.cells.append(cell)