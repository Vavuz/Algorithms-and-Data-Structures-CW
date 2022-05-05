'''
This file contains the Game class
@author Marco Vavassori
'''


class Game():
    ''' This class stores a game '''
    def __init__(self, name: str, size: int, moves: list[tuple[str, str]], allCellsStatusAndContent: list[list[bool], list[int]]):
        self.name = name
        self.size = size
        self.moves = moves
        self.allCellsStatusAndContent = allCellsStatusAndContent
