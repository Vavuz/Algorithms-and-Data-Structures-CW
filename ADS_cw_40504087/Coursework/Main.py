'''
This file is the main file for the Sudoku game
@author Marco Vavassori
@date 04/02/2022
'''
from Board import Board

# Main
sudokuBoard: Board = Board(3, 4)
print(str(sudokuBoard.getWidth()))
