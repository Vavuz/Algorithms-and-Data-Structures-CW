'''
This file contains the GameManager class
@author Marco Vavassori
'''


import time
import pickle
from datetime import date
from Game import Game
import os.path



class GameManager():
    ''' This class manages undo, redo, saving, and replaying '''

    def __init__(self, size: int):
        ''' Constructor '''
        self.moves: list[tuple[str, str]] = []
        self.movesCopy: list[tuple[str, str]] = []
        self.movesForReplay: list[tuple[str, str]] = []
        self.undoneMoves: list[tuple[str, str]] = []
        self.size = size

    
    def move(self, move: tuple[str, str]):
        ''' Updates the list of movements '''
        self.moves.append(move)
        self.movesCopy.append(move)
        self.movesForReplay.append(move)

    def getUndo(self) -> tuple[str, str]:
        ''' Returns the previous move'''
        allCoords: list[str] = []        
        lastMove: tuple[str, str] = self.movesCopy.pop()    # storing last move
        self.undoneMoves.append(lastMove)

        for coordinate in self.movesCopy:
            allCoords.append(coordinate[0])

        # In case that cell has been edited earlier
        if allCoords.count(lastMove[0].upper()) > 0 or allCoords.count(lastMove[0].lower()) > 0:
            overwriteMoves: list[list[int, tuple[str, str]]] = []
            # Looking for the moves that changed that cell earlier in the game
            for i in range(len(self.movesCopy)):
                if self.movesCopy[i][0].lower() == lastMove[0].lower():
                    moveAndIndex: list[int, tuple(str, str)] = [i, self.movesCopy[i]]
                    overwriteMoves.append(moveAndIndex)
            newMove: tuple[str, str] = overwriteMoves[len(overwriteMoves) - 1][1]    # the last editing move is picked
            return newMove
        # In case that cell has not been edited earlier
        else:
            lastMoveList = list(lastMove)
            lastMoveList[1] = 0
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


    def serialise(self, allCellsStatusAndContent: list[list[bool], list[int]]):
        ''' It serialises a list of Games into a pickle file'''

        # If the file exists I read it, otherwise I do not
        fileContent: list[Game] = []
        if os.path.exists("matches.pkl"):
            fileContent: list[Game] = self.deserialise()

        # Getting the names
        names: list[str] = []
        if len(fileContent) > 0:
            for game in fileContent:
                names.append(game.name)

        # Giving a name to the match
        while True:
            try:
                name: str = str(input("\n\nGive it a name, so you can recognise this game if you want to replay it: "))
                if names.count(name) > 0:
                    print("Sorry! This name has already been used!")
                else:
                    break
            except:
                print("This is not a valid input!")
        
        gameToAppend: Game = Game(name, self.size, self.movesForReplay, allCellsStatusAndContent)
        fileContent.append(gameToAppend)

        # Writing to file
        with open("matches.pkl", "wb") as file:
            return pickle.dump(fileContent, file)


    def deserialise(self) -> list[Game]:
        ''' It deserialises a list of Games from a pickle file'''
        with open("matches.pkl", "rb") as file:
            return pickle.load(file)