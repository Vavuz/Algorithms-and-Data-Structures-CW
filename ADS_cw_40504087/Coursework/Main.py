'''
This file is the main file for the Sudoku game
@author Marco Vavassori
@date 04/02/2022
'''
import Board

def menu():
    '''Prints the game's menu'''
    print("Welcome to Vavassudoku!")

    # Difficulty level choice
    while True:
        try:
            choice: int = int(input("\n\nChoose the difficulty level! 1/2/3: "))
            print(choice)
            if (choice == 1):
                startGame(3, 3)
                break
            elif choice == 2:
                startGame(9, 9)
                break
            elif choice == 3:
                startGame(12, 12)
                break
            else:
                print(str(choice) + " is not an option! Try again!")
        except:
            print("That is not a choice! Try again!")

def startGame(width: int, height: int):
    sudokuBoard: Board = Board(width, height)
    print("done cmon")

if __name__ == "__main__":
    menu()
