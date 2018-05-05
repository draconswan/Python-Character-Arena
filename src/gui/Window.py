"""

"""
import os
from tkinter import *
from functools import partial
from PIL import Image, ImageTk
from gui.CharacterWindow import CharacterWindow
from classes.Arena import Arena
from classes.Character import Character

maxSize = 256, 256


class Window(Frame):

    def __init__(self, characters, opponents, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.characters = characters
        self.opponents = opponents
        self.arena = Arena()
        self.init_window()

    def init_window(self):
        self.master.title("Character Battle Arena")
        self.pack(fill=BOTH, expand=1)
        self.buildMenu()
        self.setBattleSection()

    def buildMenu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu, tearoff=0)
        players = Menu(file, tearoff=0)
        players.add_command(label="Create New", command=self.createNewPlayer)
        for key in self.characters:
            players.add_command(label=key, command=partial(self.addPlayer, self.characters[key]))
        file.add_cascade(label="Add Player", menu=players)
        opponents = Menu(file, tearoff=0)
        for key in self.opponents:
            opponents.add_command(label=key, command=partial(self.addOpponent, self.opponents[key]))
        # opponents.add_command(label="Ogre", command=partial(self.addOpponent, "ogre"))
        # opponents.add_command(label="Giant", command=partial(self.addOpponent, "giant"))
        file.add_cascade(label="Add Opponent", menu=opponents)
        file.add_command(label="Exit", command=self.clientExit)
        menu.add_cascade(label="File", menu=file)

    def addPlayerImage(self, imageLoc):
        #imagePath = "images/" + characterName + ".jpg"
        if os.path.exists(imageLoc):
            character = Image.open(imageLoc)
        else:
            character = Image.open("gui/images/fighter.jpg")

        character.thumbnail(maxSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(character)

        img = Label(self, image=render, bg="blue")
        img.image = render
        xCoord = ((256 - character.size[0]) / 2)
        yCoord = ((256 - character.size[1]) / 2)
        img.place(x=xCoord, y=yCoord)
        pass

    def addOpponentImage(self, imageLoc):
        #imagePath = "images/" + opponentName + ".jpg"
        if os.path.exists(imageLoc):
            opponent = Image.open(imageLoc)
        else:
            opponent = Image.open("gui/images/goblin.jpg")

        opponent.thumbnail(maxSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(opponent)

        img = Label(self, image=render, bg="red")
        img.image = render
        xCoord = ((256 - opponent.size[0]) / 2)
        yCoord = ((256 - opponent.size[1]) / 2)
        img.place(x=(1024 - opponent.size[0] - xCoord), y=yCoord)
        pass

    def setBattleSection(self):
        Label(self, text="Character Battle Arena").pack()
        Button(self, text="").pack()

    def clientExit(self):
        exit()

    def createNewPlayer(self):
        secondWindow = Toplevel(self.master)
        CharacterWindow(self, secondWindow)

    def addPlayer(self, character):
        self.addPlayerImage(character.imageLoc)

        x1 = 0
        x2 = 125
        startingY = 266

        nameLabel = Label(self, text="Character Name").place(x=x1, y=startingY)
        nameValue = Label(self, text=character.characterName).place(x=x2, y=startingY)
        startingY += 20

        classNameLabel = Label(self, text="Character Class").place(x=x1, y=startingY)
        classNameValue = Label(self, text=character.characterClass).place(x=x2, y=startingY)
        startingY += 20

        strengthLabel = Label(self, text="Strength").place(x=x1, y=startingY)
        strengthValue = Label(self, text=character.strength).place(x=x2, y=startingY)
        startingY += 20

        quicknessLabel = Label(self, text="Quickness").place(x=x1, y=startingY)
        quicknessValue = Label(self, text=character.quickness).place(x=x2, y=startingY)
        startingY += 20

        healthLabel = Label(self, text="Health").place(x=x1, y=startingY)
        healthValue = Label(self, text=character.health).place(x=x2, y=startingY)
        startingY += 20

        armorLabel = Label(self, text="Armor").place(x=x1, y=startingY)
        armorValue = Label(self, text=character.armor).place(x=x2, y=startingY)
        startingY += 20

    def addOpponent(self, opponent):
        self.addOpponentImage(opponent.imageLoc)

        x1 = 768
        x2 = 896
        startingY = 266

        nameLabel = Label(self, text="Name").place(x=x1, y=startingY)
        nameValue = Label(self, text=opponent.characterName).place(x=x2, y=startingY)
        startingY += 20

        classNameLabel = Label(self, text="Class").place(x=x1, y=startingY)
        classNameValue = Label(self, text=opponent.characterClass).place(x=x2, y=startingY)
        startingY += 20

        strengthLabel = Label(self, text="Strength").place(x=x1, y=startingY)
        strengthValue = Label(self, text=opponent.strength).place(x=x2, y=startingY)
        startingY += 20

        quicknessLabel = Label(self, text="Quickness").place(x=x1, y=startingY)
        quicknessValue = Label(self, text=opponent.quickness).place(x=x2, y=startingY)
        startingY += 20

        healthLabel = Label(self, text="Health").place(x=x1, y=startingY)
        healthValue = Label(self, text=opponent.health).place(x=x2, y=startingY)
        startingY += 20

        armorLabel = Label(self, text="Armor").place(x=x1, y=startingY)
        armorValue = Label(self, text=opponent.armor).place(x=x2, y=startingY)
        startingY += 20
