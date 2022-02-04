'''
This file contains the Cell class
@author Marco Vavassori
@date 04/02/2022
'''

from lib2to3.pgen2.token import NEWLINE


class Cell():
    '''This class manages the cells'''

    def __init__(self, id: int, correctNumber: int):
        '''Cell class constructor'''
        self.id: int = id
        self.correctNumber: int = correctNumber
        self.currentNumber: int = None

    def drawCell(self):
        print("[ x ]", end="")
        
    def writeNumber(self, number: int):
        '''Changes the number that is currently displayed'''
        self.currentNumber = number

    def getCorrectNumber(self) -> int:
        '''Returns the number that should be in the cell'''
        return self.correctNumber