'''
This file contains the Board class
@author Marco Vavassori
@date 04/02/2022
'''

from Cell import Cell


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
    
    def drawBoard(self):
        '''Draws the board'''
        line: str = "-" * (self.width * 5)
        print("\n" + line)
        newEndLineCounter: int = 0
        linesCounter: int = 0
        for cell in self.cells:
            cell.drawCell()
            newEndLineCounter += 1
            if newEndLineCounter == self.width and linesCounter < self.width:
                print("\n")
                newEndLineCounter = 0
            elif linesCounter == self.width:
                break
        print(line)
    
    def boardUpdate(self, x: str, y: str, number: int, width: int):
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