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

root = Tk()

root.geometry("1024x768")


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
        self.showText()

    def buildMenu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu, tearoff=0)
        players = Menu(file, tearoff=0)
        players.add_command(label="Create New", command=self.createNewPlayer)
        for player in self.characters:
            players.add_command(label=player.characterClass, command=partial(self.addPlayer, player))
        file.add_cascade(label="Add Player", menu=players)
        opponents = Menu(file, tearoff=0)
        for opponent in self.opponents:
            opponents.add_command(label=opponent.characterClass, command=partial(self.addOpponent, opponent))
        # opponents.add_command(label="Ogre", command=partial(self.addOpponent, "ogre"))
        # opponents.add_command(label="Giant", command=partial(self.addOpponent, "giant"))
        file.add_cascade(label="Add Opponent", menu=opponents)
        file.add_command(label="Exit", command=self.clientExit)
        menu.add_cascade(label="File", menu=file)

    def addPlayerImage(self, characterName):
        imagePath = "images/" + characterName + ".jpg"
        if os.path.exists(imagePath):
            character = Image.open(imagePath)
        else:
            character = Image.open("images/fighter.jpg")

        character.thumbnail(maxSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(character)

        img = Label(self, image=render, bg="blue")
        img.image = render
        xCoord = ((256 - character.size[0]) / 2)
        yCoord = ((256 - character.size[1]) / 2)
        img.place(x=xCoord, y=yCoord)
        pass

    def addOpponentImage(self, opponentName):
        imagePath = "images/" + opponentName + ".jpg"
        if os.path.exists(imagePath):
            opponent = Image.open(imagePath)
        else:
            opponent = Image.open("images/goblin.jpg")

        opponent.thumbnail(maxSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(opponent)

        img = Label(self, image=render, bg="red")
        img.image = render
        xCoord = ((256 - opponent.size[0]) / 2)
        yCoord = ((256 - opponent.size[1]) / 2)
        img.place(x=(1024 - opponent.size[0] - xCoord), y=yCoord)
        pass

    def showText(self):
        text = Label(self, text="Character Battle Arena")
        text.pack()

    def clientExit(self):
        exit()

    def createNewPlayer(self):
        secondWindow = Toplevel(root)
        CharacterWindow(self, secondWindow)

    def addPlayer(self, character):
        self.addPlayerImage(character.characterName)

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
        self.addOpponentImage(opponent.characterName)

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


fighter = Character()
fighter.characterName = "Gladstone Wolfsbane"
fighter.characterClass = "Fighter"
fighter.strength = 6
fighter.quickness = 4
fighter.armor = 20
fighter.health = 40

goblin = Character()
goblin.characterName = "Wormtooth"
goblin.characterClass = "Goblin Warrior"
goblin.strength = 4
goblin.quickness = 6
goblin.armor = 14
goblin.health = 30

app = Window([fighter], [goblin], root)
root.mainloop()
