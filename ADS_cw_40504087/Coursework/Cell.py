'''
This file contains the Cell class
@author Marco Vavassori
@date 04/02/2022
'''

from enum import Enum, auto
from colorama import Fore
from termcolor import colored



class CellStatus(Enum):
    '''Status of a cell'''
    SHOWN = auto()            # number shown
    NO_GUESS = auto()         # not attempted
    CORRECT_GUESS = auto()    # correct guess
    WRONG_GUESS = auto()      # wrong guess

class Cell():
    '''This class manages the cells'''
    
    def __init__(self, id: int, correctNumber: int):
        '''Cell class constructor'''
        self.id: int = id
        self.status: CellStatus = auto()
        self.correctNumber: int = correctNumber
        self.currentNumber: int = 0

    def drawCell(self):
        '''Draws a cell'''
        if self.currentNumber == 0:
            print("[   ]", end="")
        else:
            print("[ " + colored(str(self.currentNumber), 'green') + " ]", end="")
        
    def writeNumber(self, number: int):
        '''Changes the number that is currently displayed'''
        self.currentNumber = number

    def getId(self) -> int:
        '''Returns the id'''
        return self.id

    def getCorrectNumber(self) -> int:
        '''Returns the number that should be in the cell'''
        return self.correctNumber

    def getCellStatus(self) -> CellStatus:
        '''Returns the cell's status'''
        return self.status
    
    def setCellStatus(self, status: CellStatus):
        '''Sets the cell's status'''
        self.status = status   