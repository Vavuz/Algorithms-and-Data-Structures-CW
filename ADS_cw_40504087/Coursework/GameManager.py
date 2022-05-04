'''
This file contains the GameManager class
@author Marco Vavassori
'''


import time


class GameManager():
    ''' This class manages undo, redo, saving, and replaying '''

    def __init__(self):
        ''' Constructor '''
        self.moves: list[tuple[str, str]] = []
        self.movesCopy: list[tuple[str, str]] = []
        self.movesForReplay: list[tuple[str, str]] = []
        self.undoneMoves: list[tuple[str, str]] = []

    
    def move(self, move: tuple[str, str]):
        ''' Updates the list of movements '''
        self.moves.append(move)
        self.movesCopy.append(move)
        self.movesForReplay.append(move)

    def getUndo(self) -> tuple[str, str]:
        ''' Returns the previous move'''
        #print("sono questi tutti: ", self.moves)
        allCoords: list[str] = []        
        lastMove: tuple[str, str] = self.movesCopy.pop()
        self.undoneMoves.append(lastMove)

        #print("allcoords is: ", allCoords)
        #print("lastmove is: ", lastMove)
        for coordinate in self.movesCopy:
            allCoords.append(coordinate[0])
        #print("allcoords now is: ", allCoords)
        # In case that cell has been edited earlier
        if allCoords.count(lastMove[0].upper()) > 0 or allCoords.count(lastMove[0].lower()) > 0:
            #print("we have found a repetition")
            overwriteMoves: list[list[int, tuple[str, str]]] = []
            # Looking for the moves that changed that cell earlier in the game
            for i in range(len(self.movesCopy)):
                #print("analysing: ", self.movesCopy[i])
                #input("let's check that this cell was edited earlier...")
                if self.movesCopy[i][0].lower() == lastMove[0].lower():
                    #print("this cell was edited before! let's procede")
                    #input("procede...")
                    moveAndIndex: list[int, tuple(str, str)] = [i, self.movesCopy[i]]
                    #print("move and index is: ", moveAndIndex)
                    overwriteMoves.append(moveAndIndex)
            # Removing the move from the list of moves, so it will not be done again when undoing
            #print("movescopy before deleting: ", self.movesCopy)
            #del self.movesCopy[overwriteMoves[len(overwriteMoves) - 1][0]]
            #print("movescopy after deleting: ", self.movesCopy)
            newMove: tuple[str, str] = overwriteMoves[len(overwriteMoves) - 1][1]
            #print("newmove is: ", newMove)
            #input("ready to return...")
            return newMove
        else:
            #print("we havent found a repetition")
            #input("press to create the tuple with 0...")
            lastMoveList = list(lastMove)
            lastMoveList[1] = 0
            #print("the move im going to return is: ", lastMoveList)
            #input("press to return the tuple with 0...")
            return tuple(lastMoveList)


    def undoRedoForReplay(self, move: tuple[str, str]):
        self.movesForReplay.append(move)


    def deleteUndone(self):
        self.undoneMoves = []


    def getRedo(self) -> tuple[str, str] | None:
        if len(self.undoneMoves) > 0:
            redoMove: tuple[str, str] = self.undoneMoves[len(self.undoneMoves) - 1]
            self.undoneMoves.pop()
            self.movesCopy.append(redoMove)
            return redoMove
        else:
            return None


    def saveMatch(self):
        pass