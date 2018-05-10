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
    # Each instance of Window imports the contents of characters and opponents csv files
    # from the Main class and a default master container is set to None
    def __init__(self, characters, opponents, master=None):
        Frame.__init__(self, master)
        # Setting up player section; these are the labels and text fields from the character csv file
        # that are displayed below the character's picture on the window
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

        # Setting up Opponent Section; these are the labels and text fields from the opponent csv file
        # that are displayed below the opponent's picture on the window
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

        # This creates the battle window (the large middle frame), with an empty list for battle messages
        # to be stored in to to be displayed later
        self.battleStatusMessages = []
        self.battleMessagesFrame = VerticalScrollingFrame(self, width=488, height=512, bd=1, relief=SUNKEN)

        # This is the parent frame that manages the window as a whole and instantiates a new copy of the Arena
        # class. This also sets the max rounds to 10
        self.master = master
        self.characters = characters
        self.opponents = opponents
        self.arena = Arena()
        self.arena.maxRounds = 10
        self.init_window()

    # Sets the size and placement of the master window and its accompanying labels
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

    # Sets the size and placement of the battle window (the large middle frame), its accompanying labels
    # and where the battle messages will be displayed
    def setBattleSection(self):
        Label(self, text="Character Battle Arena").pack()
        Button(self, text="Start Battle", command=self.startBattle).pack()
        self.battleMessagesFrame.pack(fill=None, expand=False, pady=(5, 0))
        Frame(self.battleMessagesFrame.interior, width=468, height=1).grid()

    # Creates the menu options of the master window, allowing the user to exit, create or choose a new character
    # player and choose and opponent player for battle
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

    # displays the image associated with the chosen character player, based on the associated location 
    # provided by the csv file. If a character is created instead of chosen, a default image is set
    def addPlayerImage(self, imageLoc):
        if os.path.exists(imageLoc):
            character = Image.open(imageLoc)
        else:
            character = Image.open("gui/images/fighter.jpg")

        character.thumbnail(maxImageSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(character)
        
        # Sets the size, placement, and background of the rendered image
        self.imageLabelPlayer['image'] = render
        self.imageLabelPlayer['bg'] = "blue"
        self.imageLabelPlayer.image = render
        xCoord = ((256 - character.size[0]) / 2)
        yCoord = ((256 - character.size[1]) / 2)
        self.imageLabelPlayer.place(x=xCoord, y=yCoord)
    
    # displays the image associated with the chosen opponent players, based on the associated location 
    # provided by the csv file. If an opponent is created instead of chosen, a default image is set
    def addOpponentImage(self, imageLoc):
        if os.path.exists(imageLoc):
            opponent = Image.open(imageLoc)
        else:
            opponent = Image.open("gui/images/goblin.jpg")

        opponent.thumbnail(maxImageSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(opponent)
        
        # Sets the size, placement, and background of the rendered image
        self.imageLabelOpponent['image'] = render
        self.imageLabelOpponent['bg'] = "red"
        self.imageLabelOpponent.image = render
        xCoord = ((256 - opponent.size[0]) / 2)
        yCoord = ((256 - opponent.size[1]) / 2)
        self.imageLabelOpponent.place(x=(1024 - opponent.size[0] - xCoord), y=yCoord)

    # Displays each of the messages in the battle message list in the messages frame interior
    def displayBattleStatusMessages(self, messages):
        for message in messages:
            battleMessagesLabel = Label(self.battleMessagesFrame.interior, text=message.message,
                                        fg=message.messageColor)
            self.battleStatusMessages.append(battleMessagesLabel)
            battleMessagesLabel.grid()

    # If a user would like to start a new battle, this method clears the messages from the screen and then
    # all of the contents of the battle status messages list
    def clearMessages(self):
        for message in self.battleStatusMessages:
            message.destroy()
        del self.battleStatusMessages[:]

    # Exits the program and closes the window
    def clientExit(self):
        exit()

    # validates that the battle can start (has one player and one opponent; throws and error message if it does not),
    # calls methods to clear any battle messages from the window, populate the arena instance 
    # and calls battle actions while the battle is still active
    def startBattle(self):
        if self.arena.isReady():
            self.clearMessages()
            self.arena.resetBattle()
            self.updatePlayer(self.arena.player)
            self.updateOpponent(self.arena.opponent)
            while True:
                self.displayBattleStatusMessages(
                    [BattleMessage("Battle Status:", "green"), self.arena.getBattleStatus()])
                battleResult = self.arena.battleRound()
                self.displayBattleStatusMessages(battleResult[1])
                self.update()
                if battleResult[0]:
                    self.updatePlayer(self.arena.player)
                    self.updateOpponent(self.arena.opponent)
                    break
                else:
                    self.updatePlayer(self.arena.player)
                    self.updateOpponent(self.arena.opponent)
                    time.sleep(1)
        else:
            messagebox.showinfo("Warning",
                                "Please make sure there are 2 participants in the arena before starting the battle")

    # When a player chooses to create their own character, this method controls the pop-up window that displays
    # by displaying it on top of the master window and initializing a new character window class
    def createNewPlayer(self):
        secondWindow = Toplevel(self.master)
        CharacterWindow(self, secondWindow)
        secondWindow.resizable(width=False, height=False)

    # Populates the image and all of the labels from the character class instance for the player
    def addPlayer(self, character):
        self.addPlayerImage(character.imageLoc)
        self.nameValuePlayer['text'] = character.characterName
        self.classNameValuePlayer['text'] = character.characterClass
        self.strengthValuePlayer['text'] = character.strength
        self.quicknessValuePlayer['text'] = character.quickness
        self.healthValuePlayer['text'] = character.health
        self.armorValuePlayer['text'] = character.armor
        self.arena.setPlayer(character)
        self.update()

    # updates the label of the opponent's current health as a fraction of their total starting health
    def updatePlayer(self, player):
        self.healthValuePlayer['text'] = "%d/%d" % (player.getCurrentHP(), player.health)
        self.update()

    # Populates the image and all of the labels from the character class instance for the opponent
    def addOpponent(self, opponent):
        self.addOpponentImage(opponent.imageLoc)
        self.nameValueOpponent['text'] = opponent.characterName
        self.classNameValueOpponent['text'] = opponent.characterClass
        self.strengthValueOpponent['text'] = opponent.strength
        self.quicknessValueOpponent['text'] = opponent.quickness
        self.healthValueOpponent['text'] = opponent.health
        self.armorValueOpponent['text'] = opponent.armor
        self.arena.setOpponent(opponent)
        self.update()

    # updates the label of the opponent's current health as a fraction of their total starting health
    def updateOpponent(self, opponent):
        self.healthValueOpponent['text'] = "%d/%d" % (opponent.getCurrentHP(), opponent.health)
        self.update()
