'''
This file is the main file for the Sudoku game
@author Marco Vavassori
@date 04/02/2022
'''

from Board import Board
from Cell import Cell


def menu():
    '''Prints the game's menu'''
    print("Welcome to Vavassudoku!")

    # Difficulty level choice
    while True:
        try:
            choice: int = int(input("\n\nChoose the difficulty level! 1/2/3: "))
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

def rules():
    print("le regole")

def startGame(width: int, height: int):
    '''Draws the sudoku board'''
    rules()
    sudokuBoard: Board = Board(width, height)
    sudokuBoard.drawBoard()
    movementLoop(sudokuBoard, width)

def movementLoop(sudokuBoard: Board, width: int):
    '''Applies the user moves'''
    while True:
        try:
            move: tuple = tuple(input("What is your next move?: ").split(','))
            if moveValidation(move, width):
                # numberInsertion()
                sudokuBoard.drawBoard()
                print("movimento valido")
            else:
                print("The input is not valid! Remember: <cell_coordinates>,<number>\n e.g. B3,4")
        except:
            print("The input is not valid! Remember: <cell_coordinates>,<number>\n e.g. B3,4")

def moveValidation(move: tuple, width: int) -> bool:
    '''Validates the user move'''
    try:
        print(ord(move[0][:1]))
        if (ord('A') <= ord(move[0][:1]) <= (ord('A') + width)) or (ord('a') <= ord(move[0][:1]) <= (ord('a') + width)):
            print(int(move[0][1:]))
            if 1 <= int(move[0][1:]) <= width:
                print(int(move[1]))
                if 1 <= int(move[1]) <= width:
                    return True
    except:
        return False
    return False


if __name__ == "__main__":
    menu()
    input("\n Enter key to escape...")
