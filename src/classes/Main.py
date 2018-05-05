'''
Created on Apr 29, 2018

@author: Erin
'''

from classes.Arena import Arena
from classes.Character import Character

def main():
    #Need to make this a loop around whole game
    gameInput = input("Would you like to start a new game? (Y/N): ")
    if gameInput.lower() in ("y", "yes"):
        buildArena()
    elif gameInput.lower() in ("n", "no"):
        print("Terminated normally")
    else:
        print("Please input Y or N")
        
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
    pass

main()
    