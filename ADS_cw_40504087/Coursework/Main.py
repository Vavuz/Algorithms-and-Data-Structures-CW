'''
This file is the main file for the Sudoku game
@author Marco Vavassori
@date 04/02/2022
'''

from Board import Board
import threading
import time
import os


def countdown():
    '''Manages the thread of the timer'''
    global sudokuTimer
    global stopThread
    for sec in range(sudokuTimer):
        sudokuTimer -= 1
        time.sleep(1)
        if stopThread:
            break  

def theme():
    '''Prints the game's name'''
    print("\n\n /\   /\__ ___   ____ _ ___ ___ _   _  __| | ___ | | ___   _       |\n" +
              " \ \ / / _` \ \ / / _` / __/ __| | | |/ _` |/ _ \| |/ / | | |      |\n" +
              "  \ V / (_| |\ V / (_| \__ \__ \ |_| | (_| | (_) |   <| |_| |      |\n" +
              "   \_/ \__,_| \_/ \__,_|___/___/\__,_|\__,_|\___/|_|\_\__,__|      |\n" +
              "                                                                   |")

def menu():
    '''Prints the game's menu'''
    theme()
    print("\t\t\tWelcome to Vavassudoku!" + 20 * ' ' + "|\n",
    "-" * 67)
    # rules()

    # Global variables setting
    global sudokuTimer

    # Difficulty level choice
    while True:
        try:
            choice: int = int(input("\n\nChoose the grid's size! 1/2 (4x4 or 9x9): "))
            # Whenever the input is an integer
            if (choice == 1):
                sudokuTimer = 361
                startGame(4, 4, choice)
                break
            elif choice == 2:
                while True:
                    try:
                        secondChoice: int = int(input("\n\nChoose the difficulty level! 1(easy)/ 2(medium)/ 3(difficult): "))
                        if secondChoice == 1:
                            sudokuTimer = 1081
                            startGame(9, 9, choice)
                            break
                        elif secondChoice == 2:
                            sudokuTimer = 781
                            startGame(9, 9, choice)
                            break
                        elif secondChoice == 3:
                            sudokuTimer = 481
                            startGame(9, 9, choice)
                            break
                        else:
                            print(str(secondChoice) + " is not an option! Try again!")
                    except:
                        print(str(secondChoice) + " is not an option! Try again!")
                break
            else:
                print(str(choice) + " is not an option! Try again!")
        # Whenever the input is not an integer
        except:
            print("That is not a choice! Try again!")


def rules():
    print("\n\n▬▬ι═══════   The rules   ═══════ι▬▬")
    time.sleep(0.5)
    print("\n The rules are very simple: ")
    time.sleep(1.5)
    print("   To insert a number into the sudoku table you will need to provide the console\n",
          "  with a coordinate (e.g. 'B3', 'e7', 'H9'), a comma ',' and a number (e.g. '1', '5', '8')\n")
    time.sleep(1.5)
    print("   Your input should look like that:   D4,2\n")
    time.sleep(1.5)
    print("   Whenever you want to read the rules, input 'R'\n")
    time.sleep(1.5)
    print("   Whenever you want to quit, input 'Q'\n")
    time.sleep(1.5)
    print(" Now that you know the rules you can start playing!\n\n",
        "▬▬ι═══════════════════════════ι▬▬")
    time.sleep(1.5)


def startGame(width: int, height: int, choice: int):
    '''Draws the sudoku board'''
    sudokuBoard: Board = Board(width, height)
    os.system('cls')
    theme()
    # Countdown is started
    countdownThread = threading.Thread(target = countdown)
    countdownThread.start()
    # Board management
    sudokuBoard.drawBoard(choice, sudokuTimer)
    movementLoop(sudokuBoard, width, choice)


def movementLoop(sudokuBoard: Board, width: int, choice: int):
    '''Applies the user moves'''
    # Global variables setting
    global sudokuTimer
    global stopThread
    stopThread = False

    while sudokuTimer > 0:
        while True:
            try:
                move: str = str(input("\nWhat is your next move?: "))

                if (move == 'R' or move == 'r'):
                    if sudokuTimer < 1:
                        break
                    os.system('cls')
                    theme()
                    sudokuBoard.drawBoard(choice, sudokuTimer)
                    rules()
                elif (move == 'Q' or move == 'q'):
                    stopThread = True
                    break
                else:
                    if sudokuTimer < 1:
                        break
                    moveTuple: tuple = tuple(move.replace(' ', '').split(','))
                    # If the move is of valid type the program can proceed to check it in deeper detail
                    if moveValidation(moveTuple, width):
                        # Checking that the cell is editable
                        if editableValidation(sudokuBoard, moveTuple, width):
                            # Checking that no number interferes
                            if uniquenessValidation(sudokuBoard, moveTuple, width):
                                sudokuBoard.boardUpdate(moveTuple[0][:1], moveTuple[0][1:], moveTuple[1], width)
                                os.system('cls')
                                theme()
                                sudokuBoard.drawBoard(choice, sudokuTimer)
                            else:
                                os.system('cls')
                                theme()
                                sudokuBoard.drawBoard(choice, sudokuTimer)
                                print("\n" + moveTuple[1] + " is already present in this row/column/block!")
                        else:
                            os.system('cls')
                            theme()
                            sudokuBoard.drawBoard(choice, sudokuTimer)
                            print("\nThis cell cannot be edited!")
                    else:
                        os.system('cls')
                        theme()
                        sudokuBoard.drawBoard(choice, sudokuTimer)
                        print("\nThe input is not valid! Remember: <cell_coordinates>,<number>\n e.g. B3,4")
            except:
                os.system('cls')
                theme()
                sudokuBoard.drawBoard(choice, sudokuTimer)
                print("\nThe input is not valid! Remember: <cell_coordinates>,<number>\n e.g. B3,4")
        break
    if sudokuTimer < 1:
        os.system('cls')
        print("\nTIME IS OUT!!!")


def moveValidation(moveTuple: tuple, width: int) -> bool:
    '''Validates the user move'''
    try:
        # Checking that the coordinate exists (letter bit)
        if (ord('A') <= ord(moveTuple[0][:1]) <= (ord('A') + width)) or (ord('a') <= ord(moveTuple[0][:1]) <= (ord('a') + width)):
            # Checking that the coordinate exists (number bit)
            if 1 <= int(moveTuple[0][1:]) <= width:
                # Checking that the number to insert is in the available range
                if 1 <= int(moveTuple[1]) <= width:
                    return True
    except:
        return False
    return False


def uniquenessValidation(sudokuBoard: Board, moveTuple: tuple, width: int) -> bool:
    '''Validates that the user's move does not interfere with other numbers'''
    idsToCheck: list[int] = []

    # Adding horizontal cells
    startingHorizontalId: int = (int(moveTuple[0][1:]) - 1) * width
    currentId: int = startingHorizontalId + sudokuBoard.coordinates[moveTuple[0][:1]] - 1

    for id in range(startingHorizontalId, startingHorizontalId + width):
        idsToCheck.append(id)

    # Adding vertical cells
    startingverticalId: int = sudokuBoard.coordinates[moveTuple[0][:1]] - 1
    for i in range(width):
        idsToCheck.append(startingverticalId)
        startingverticalId += width
        
    # Adding block cells
    startingBlockId: int = currentId
    if width == 9:
        # If we are working with the 9x9 grid
        while True:
            if 0 <= startingBlockId < 9 or 27 <= startingBlockId < 36 or 54 <= startingBlockId < 63:
                # This cell is in the first column of the block
                if startingBlockId % 3 == 0:
                    # This cell is the first cell of the block
                    break
                else:
                    startingBlockId -= 1
            else:
                startingBlockId -= 9
        # The block cell's ids are added        
        for i in range(3):
            idsToCheck.append(startingBlockId)
            for j in range(1, 3):
                idsToCheck.append(startingBlockId + j)
            startingBlockId += 9
    else:
        # if we are working with the 4x4 grid
        while True:
            if 0 <= startingBlockId < 4 or 8 <= startingBlockId < 12:
                # This cell is in the first column of the block
                if startingBlockId % 2 == 0:
                    # This cell is the first cell of the block
                    break
                else:
                    startingBlockId -= 1
            else:
                startingBlockId -= 4
        # The block cell's ids are added             
        for i in range(2):
            idsToCheck.append(startingBlockId)
            for j in range(2):
                idsToCheck.append(startingBlockId + j)
            startingBlockId += 4

    # Removing duplicates and the cell that we are filling in
    idsToCheck = list(dict.fromkeys(idsToCheck))
    idsToCheck.remove(currentId)
    
    # Total check
    idsToCheck.sort()
    
    for cell in sudokuBoard.cells:
        # The cells that have one of the ids in the idsToCheck list are checked
        if cell.id == idsToCheck[0]:
            idsToCheck = idsToCheck[1:]
            if str(cell.currentNumber) == moveTuple[1]:
                # If the is an interference false is returned
                return False
        if len(idsToCheck) == 0:
            break
    return True


def editableValidation(sudokuBoard: Board, moveTuple: tuple, width: int) -> bool:
    '''Validates that the cell can be edited'''
    currentId: int = ((int(moveTuple[0][1:]) - 1) * width) + sudokuBoard.coordinates[moveTuple[0][:1]] - 1
    for cell in sudokuBoard.cells:
        if cell.id == currentId:
            if cell.overwritable == True:
                return True
            else:
                return False



if __name__ == "__main__":
    #os.system("color 1f")
    stopThread = False
    menu()
    stopThread = True
    input("\n\n Enter key to escape...")
