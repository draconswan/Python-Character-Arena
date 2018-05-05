'''
Created on Apr 29, 2018

@author: Erin
'''
from classes.Arena import Arena
from classes.Character import Character
from gui.Window import Window
from tkinter import *
import csv



def main():
    opponents = {}
    players = {}
    #Need to make this a loop around whole game
    with open('opponents.csv', 'r') as opponentsFile:
        opponentList = csv.reader(opponentsFile, delimiter = ",")
        
        for row in opponentList:
            opponent = Character(row[0], row[1], row[2], row[3], row[4])
            opponents[row[1]] = opponent

    with open('players.csv', 'r') as playersFile:
        playersList = csv.reader(playersFile, delimiter = ",")
        for row in playersList:
            player = Character(row[0], row[1], row[2], row[3], row[4])
            players[row[1]] = player
    
    opponentsFile.close()
    playersFile.close()
    root = Tk()

    root.geometry("1024x768")

    app = Window(players, opponents, root)
    root.mainloop()
'''
    gameInput = input("Would you like to start a new game? (Y/N): ")
    if gameInput.lower() in ("y", "yes"):
        buildArena()
    elif gameInput.lower() in ("n", "no"):
        print("Terminated normally")
    else:
        print("Please input Y or N")
 '''   

        
def buildArena():
    #ask player to select a character
        #ask player to select weapon
    playerOne = Character("Character","Fighter", 5, 5, 18, 20)
    
    #ask player to select an opponent
    playerTwo = Character("Opponent", "Fighter", 5, 5, 5, 100)

    #Start Battle
    newBattle = Arena()
    newBattle.setPlayer(playerOne)
    newBattle.setOpponent(playerTwo)
    newBattle.startBattle()
    newBattle.getBattleStatus()
    
    

def endGame():
    #display game summary; loop to new game choice
    opponents.close()
    players.close()

main()
    