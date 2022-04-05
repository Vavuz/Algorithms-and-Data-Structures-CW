'''
This file is the main file for the Sudoku game
@author Marco Vavassori
@date 04/02/2022
'''

from Board import Board
from Cell import Cell
import time
import os


def theme():
    '''Prints the game's name'''
    print("\n /\   /\__ ___   ____ _ ___ ___ _   _  __| | ___ | | ___   _       |\n"
          " \ \ / / _` \ \ / / _` / __/ __| | | |/ _` |/ _ \| |/ / | | |      |\n"
          "  \ V / (_| |\ V / (_| \__ \__ \ |_| | (_| | (_) |   <| |_| |      |\n"
          "   \_/ \__,_| \_/ \__,_|___/___/\__,_|\__,_|\___/|_|\_\\__,_|       |\n",
          "                                                                  |")

def menu():
    '''Prints the game's menu'''
    theme()
    print("\t\t    Welcome to Vavassudoku!                        |\n",
    "-" * 67)

    # Difficulty level choice
    while True:
        try:
            choice: int = int(input("\n\nChoose the difficulty level! 1/2/3: "))
            # Whenever the input is an integer
            if (choice == 1):
                startGame(4, 4, choice)
                break
            elif choice == 2:
                startGame(9, 9, choice)
                break
            elif choice == 3:
                startGame(16, 16, choice)
                break
            else:
                print(str(choice) + " is not an option! Try again!")
        # Whenever the input is not an integer
        except:
            print("That is not a choice! Try again!")

def rules():
    print("\n\n▬▬ι═══════   The rules   ═══════ι▬▬")
    time.sleep(0.5)
    print(" The rules are very simple: ")
    time.sleep(1.5)
    print("   To insert a number into the sudoku table you will need to provide the console\n",
          "  with a coordinate (e.g. B3, e7, H9) and a number (e.g. 1, 5, 12)\n")
    time.sleep(1.5)
    print("   Your input should look like that:   F4,2\n")
    time.sleep(1.5)
    print(" Now that you are aware of the rules you can start playing!\n",
        "▬▬ι═══════════════════════════ι▬▬")
    time.sleep(1.5)

def startGame(width: int, height: int, choice: int):
    '''Draws the sudoku board'''
    #rules()
    sudokuBoard: Board = Board(width, height)
    sudokuBoard.drawBoard(choice)
    movementLoop(sudokuBoard, width, choice)

def movementLoop(sudokuBoard: Board, width: int, choice: int):
    '''Applies the user moves'''
    while True:
        try:
            move: tuple = tuple(input("\nWhat is your next move?: ").split(','))
            if moveValidation(move, width):
                sudokuBoard.boardUpdate(move[0][:1], move[0][1:], move[1], width)
                os.system('cls')
                theme()
                sudokuBoard.drawBoard(choice)
            else:
                print("The input is not valid! Remember: <cell_coordinates>,<number>\n e.g. B3,4")
        except:
            print("The input is not valid! Remember: <cell_coordinates>,<number>\n e.g. B3,4")

def moveValidation(move: tuple, width: int) -> bool:
    '''Validates the user move'''
    try:
        # Checking that the coordinate exists (letter bit)
        if (ord('A') <= ord(move[0][:1]) <= (ord('A') + width)) or (ord('a') <= ord(move[0][:1]) <= (ord('a') + width)):
            # Checking that the coordinate exists (number bit)
            if 1 <= int(move[0][1:]) <= width:
                # Checking that the number to insert is in the available range
                if 1 <= int(move[1]) <= width:
                    return True
    except:
        return False
    return False


if __name__ == "__main__":
    menu()
    input("\n Enter key to escape...")
