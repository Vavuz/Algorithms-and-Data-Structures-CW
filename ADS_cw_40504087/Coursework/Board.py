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
        self.cells: list[Cell] = None

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