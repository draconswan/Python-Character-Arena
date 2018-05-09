'''
Created on Apr 29, 2018

@author: Erin
'''
from classes.Character import Character
from gui.Window import Window
from tkinter import Tk
import csv


def main():
    opponents = {}
    players = {}
    # Need to make this a loop around whole game
    with open('opponents.csv', 'r') as opponentsFile:
        opponentList = csv.reader(opponentsFile, delimiter=",")
        for row in opponentList:
            opponent = Character(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), row[6])
            opponents[row[1]] = opponent

    with open('players.csv', 'r') as playersFile:
        playersList = csv.reader(playersFile, delimiter=",")
        for row in playersList:
            player = Character(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), row[6])
            players[row[1]] = player

    opponentsFile.close()
    playersFile.close()
    root = Tk()
    root.geometry("1024x768")
    root.resizable(width=False, height=False)

    Window(players, opponents, root)
    root.mainloop()

main()
