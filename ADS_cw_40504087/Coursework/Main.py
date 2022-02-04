'''
This file is the main file for the Sudoku game
@author Marco Vavassori
@date 04/02/2022
'''

from Board import Board
from Cell import Cell
import time


def menu():
    '''Prints the game's menu'''
    print("Welcome to Vavassudoku!")

    # Difficulty level choice
    while True:
        try:
            choice: int = int(input("\n\nChoose the difficulty level! 1/2/3: "))
            print(choice)
            # Whenever the input is an integer
            if (choice == 1):
                startGame(4, 4)
                break
            elif choice == 2:
                startGame(9, 9)
                break
            elif choice == 3:
                startGame(16, 16)
                break
            else:
                print(str(choice) + " is not an option! Try again!")
        # Whenever the input is not an integer
        except:
            print("That is not a choice! Try again!")

def startGame(width: int, height: int):
    '''Draws the sudoku board'''
    sudokuBoard: Board = Board(width, height)
    sudokuBoard.drawBoard()
    input("Press a key to escape...")

if __name__ == "__main__":
    menu()
