'''
This file contains the Cell class
@author Marco Vavassori
@date 04/02/2022
'''

from termcolor import colored


class Cell():
    '''This class manages the cells'''
    
    def __init__(self, id: int, overwritable: bool, currentNumber: int):
        '''Cell class constructor'''
        self.id: int = id
        self.overwritable: bool = overwritable
        self.currentNumber: int = currentNumber


    def drawCell(self):
        '''Draws a cell'''
        if self.currentNumber == 0:
            print("[   ]", end="")
        else:
            if self.overwritable:
                print("[ " + colored(str(self.currentNumber), 'green') + " ]", end="")
            else:
                print("[ " + colored(str(self.currentNumber), 'cyan') + " ]", end="")
        

    def writeNumber(self, number: int):
        '''Changes the number that is currently displayed'''
        self.currentNumber = number


    def getId(self) -> int:
        '''Returns the id'''
        return self.id 