"""
Created on 5/2/18

@author:   Daniel Swan & Erin Swan
@email:    ds235410@my.stchas.edu & es209931@my.stchas.edu
"""
import os
import time
from functools import partial
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

from classes.Arena import Arena
from gui.CharacterWindow import CharacterWindow
from classes.BattleMessage import BattleMessage
from gui.VerticalScrollingFrame import VerticalScrollingFrame

maxImageSize = 256, 256


class Window(Frame):

    def __init__(self, characters, opponents, master=None):
        Frame.__init__(self, master)
        # Setting up player section
        self.imageLabelPlayer = Label(self)
        self.armorLabelPlayer = Label(self, text="Armor")
        self.armorValuePlayer = Label(self, text="")
        self.healthLabelPlayer = Label(self, text="Health")
        self.healthValuePlayer = Label(self, text="")
        self.quicknessLabelPlayer = Label(self, text="Quickness")
        self.quicknessValuePlayer = Label(self, text="")
        self.strengthLabelPlayer = Label(self, text="Strength")
        self.strengthValuePlayer = Label(self, text="")
        self.classNameLabelPlayer = Label(self, text="Class")
        self.classNameValuePlayer = Label(self, text="")
        self.nameLabelPlayer = Label(self, text="Name")
        self.nameValuePlayer = Label(self, text="")

        # Setting up Opponent Section
        self.imageLabelOpponent = Label(self)
        self.armorLabelOpponent = Label(self, text="Armor")
        self.armorValueOpponent = Label(self, text="")
        self.healthLabelOpponent = Label(self, text="Health")
        self.healthValueOpponent = Label(self, text="")
        self.quicknessLabelOpponent = Label(self, text="Quickness")
        self.quicknessValueOpponent = Label(self, text="")
        self.strengthLabelOpponent = Label(self, text="Strength")
        self.strengthValueOpponent = Label(self, text="")
        self.classNameLabelOpponent = Label(self, text="Class")
        self.classNameValueOpponent = Label(self, text="")
        self.nameLabelOpponent = Label(self, text="Name")
        self.nameValueOpponent = Label(self, text="")

        # Battle Window
        self.battleStatusMessages = []
        self.battleMessagesFrame = VerticalScrollingFrame(self, width=488, height=512, bd=1, relief=SUNKEN)

        self.master = master
        self.characters = characters
        self.opponents = opponents
        self.arena = Arena()
        self.arena.maxRounds = 10
        self.init_window()

    def init_window(self):
        self.master.title("Character Battle Arena")
        self.pack(fill=BOTH, expand=1)
        self.buildMenu()
        self.setBattleSection()
        x1 = 0
        x2 = 125
        x3 = 768
        x4 = 896
        startingY = 266

        self.imageLabelPlayer.place(x=0, y=0)
        self.imageLabelOpponent.place(x=0, y=0)
        self.nameLabelPlayer.place(x=x1, y=startingY)
        self.nameValuePlayer.place(x=x2, y=startingY)
        self.nameLabelOpponent.place(x=x3, y=startingY)
        self.nameValueOpponent.place(x=x4, y=startingY)
        startingY += 20

        self.classNameLabelPlayer.place(x=x1, y=startingY)
        self.classNameValuePlayer.place(x=x2, y=startingY)
        self.classNameLabelOpponent.place(x=x3, y=startingY)
        self.classNameValueOpponent.place(x=x4, y=startingY)
        startingY += 20

        self.strengthLabelPlayer.place(x=x1, y=startingY)
        self.strengthValuePlayer.place(x=x2, y=startingY)
        self.strengthLabelOpponent.place(x=x3, y=startingY)
        self.strengthValueOpponent.place(x=x4, y=startingY)
        startingY += 20

        self.quicknessLabelPlayer.place(x=x1, y=startingY)
        self.quicknessValuePlayer.place(x=x2, y=startingY)
        self.quicknessLabelOpponent.place(x=x3, y=startingY)
        self.quicknessValueOpponent.place(x=x4, y=startingY)
        startingY += 20

        self.healthLabelPlayer.place(x=x1, y=startingY)
        self.healthValuePlayer.place(x=x2, y=startingY)
        self.healthLabelOpponent.place(x=x3, y=startingY)
        self.healthValueOpponent.place(x=x4, y=startingY)
        startingY += 20

        self.armorLabelPlayer.place(x=x1, y=startingY)
        self.armorValuePlayer.place(x=x2, y=startingY)
        self.armorLabelOpponent.place(x=x3, y=startingY)
        self.armorValueOpponent.place(x=x4, y=startingY)
        startingY += 20

    def setBattleSection(self):
        Label(self, text="Character Battle Arena").pack()
        Button(self, text="Start Battle", command=self.startBattle).pack()
        self.battleMessagesFrame.pack(fill=None, expand=False, pady=(5, 0))
        Frame(self.battleMessagesFrame.interior, width=468, height=1).grid()

    def buildMenu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu, tearoff=0)
        players = Menu(file, tearoff=0)
        players.add_command(label="Create New", command=self.createNewPlayer)
        players.add_separator()
        for key in self.characters:
            players.add_command(label=key, command=partial(self.addPlayer, self.characters[key]))
        file.add_cascade(label="Add Player", menu=players)
        opponents = Menu(file, tearoff=0)
        for key in self.opponents:
            opponents.add_command(label=key, command=partial(self.addOpponent, self.opponents[key]))
        file.add_cascade(label="Add Opponent", menu=opponents)
        file.add_separator()
        file.add_command(label="Exit", command=self.clientExit)
        menu.add_cascade(label="File", menu=file)

    def addPlayerImage(self, imageLoc):
        if os.path.exists(imageLoc):
            character = Image.open(imageLoc)
        else:
            character = Image.open("gui/images/fighter.jpg")

        character.thumbnail(maxImageSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(character)

        self.imageLabelPlayer['image'] = render
        self.imageLabelPlayer['bg'] = "blue"
        self.imageLabelPlayer.image = render
        xCoord = ((256 - character.size[0]) / 2)
        yCoord = ((256 - character.size[1]) / 2)
        self.imageLabelPlayer.place(x=xCoord, y=yCoord)

    def addOpponentImage(self, imageLoc):
        if os.path.exists(imageLoc):
            opponent = Image.open(imageLoc)
        else:
            opponent = Image.open("gui/images/goblin.jpg")

        opponent.thumbnail(maxImageSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(opponent)

        self.imageLabelOpponent['image'] = render
        self.imageLabelOpponent['bg'] = "red"
        self.imageLabelOpponent.image = render
        xCoord = ((256 - opponent.size[0]) / 2)
        yCoord = ((256 - opponent.size[1]) / 2)
        self.imageLabelOpponent.place(x=(1024 - opponent.size[0] - xCoord), y=yCoord)

    def displayBattleStatusMessages(self, messages):
        for message in messages:
            battleMessagesLabel = Label(self.battleMessagesFrame.interior, text=message.message,
                                        fg=message.messageColor)
            self.battleStatusMessages.append(battleMessagesLabel)
            battleMessagesLabel.grid()

    def clearMessages(self):
        for message in self.battleStatusMessages:
            message.destroy()

    def clientExit(self):
        exit()

    def startBattle(self):
        if self.arena.isReady():
            self.clearMessages()
            self.arena.resetBattle()
            self.updatePlayer(self.arena.player)
            self.updateOpponent(self.arena.opponent)
            self.displayBattleStatusMessages([self.arena.getBattleStatus()])
            while True:
                battleResult = self.arena.battleRound()
                self.displayBattleStatusMessages(battleResult[1])
                self.update()
                if battleResult[0]:
                    self.updatePlayer(self.arena.player)
                    self.updateOpponent(self.arena.opponent)
                    break
                else:
                    self.displayBattleStatusMessages(
                        [BattleMessage("Battle Status:", "green"), self.arena.getBattleStatus()])
                    self.updatePlayer(self.arena.player)
                    self.updateOpponent(self.arena.opponent)
                    time.sleep(1)
        else:
            messagebox.showinfo("Warning",
                                "Please make sure there are 2 participants in the arena before starting the battle")

    def createNewPlayer(self):
        secondWindow = Toplevel(self.master)
        CharacterWindow(self, secondWindow)
        secondWindow.resizable(width=False, height=False)

    def addPlayer(self, character):
        self.addPlayerImage(character.imageLoc)
        self.nameValuePlayer['text'] = character.characterName
        self.classNameValuePlayer['text'] = character.characterClass
        self.strengthValuePlayer['text'] = character.strength
        self.quicknessValuePlayer['text'] = character.quickness
        self.healthValuePlayer['text'] = character.health
        self.armorValuePlayer['text'] = character.armor
        self.arena.setPlayer(character)

    def updatePlayer(self, player):
        self.healthValuePlayer['text'] = "%d/%d" % (player.getCurrentHP(), player.health)

    def addOpponent(self, opponent):
        self.addOpponentImage(opponent.imageLoc)
        self.nameValueOpponent['text'] = opponent.characterName
        self.classNameValueOpponent['text'] = opponent.characterClass
        self.strengthValueOpponent['text'] = opponent.strength
        self.quicknessValueOpponent['text'] = opponent.quickness
        self.healthValueOpponent['text'] = opponent.health
        self.armorValueOpponent['text'] = opponent.armor
        self.arena.setOpponent(opponent)

    def updateOpponent(self, opponent):
        self.healthValueOpponent['text'] = "%d/%d" % (opponent.getCurrentHP(), opponent.health)
