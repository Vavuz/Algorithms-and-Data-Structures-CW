'''
This file contains the Cell class
@author Marco Vavassori
@date 04/02/2022
'''

from enum import Enum, auto


class CellStatus(Enum):
   SHOWN = auto()            # number shown
   NO_GUESS = auto()         # not attempted
   CORRECT_GUESS = auto()    # correct guess
   WRONG_GUESS = auto()      # wrong guess

class Cell():
    '''This class manages the cells'''

    def __init__(self, id: int, correctNumber: int):
        '''Cell class constructor'''
        self.id: int = id
        self.correctNumber: int = correctNumber
        self.currentNumber: int = None

    def drawCell(self):
        if self.currentNumber == None:
            print("[   ]", end="")
        else:
            print("[ " + str(self.currentNumber) + " ]", end="")
        
    def writeNumber(self, number: int):
        '''Changes the number that is currently displayed'''
        self.currentNumber = number

    def getCorrectNumber(self) -> int:
        '''Returns the number that should be in the cell'''
        return self.correctNumber