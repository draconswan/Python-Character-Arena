"""

"""
import os
from functools import partial
from tkinter import *

from PIL import Image, ImageTk

from classes.Arena import Arena
from gui.CharacterWindow import CharacterWindow

maxImageSize = 256, 256


class Window(Frame):

    def __init__(self, characters, opponents, master=None):
        Frame.__init__(self, master)
        # Setting up player section
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
        x1 = 0
        x2 = 125
        x3 = 768
        x4 = 896
        startingY = 266

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

    def addPlayerImage(self, characterName, imageLoc):
        # imagePath = "images/" + characterName + ".jpg"
        if os.path.exists(imageLoc):
            character = Image.open(imageLoc)
        else:
            character = Image.open("gui/images/fighter.jpg")

        character.thumbnail(maxImageSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(character)

        img = Label(self, image=render, bg="blue")
        img.image = render
        xCoord = ((256 - character.size[0]) / 2)
        yCoord = ((256 - character.size[1]) / 2)
        img.place(x=xCoord, y=yCoord)
        pass

    def addOpponentImage(self, opponentName, imageLoc):
        # imagePath = "images/" + opponentName + ".jpg"
        if os.path.exists(imageLoc):
            opponent = Image.open(imageLoc)
        else:
            opponent = Image.open("gui/images/goblin.jpg")

        opponent.thumbnail(maxImageSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(opponent)

        img = Label(self, image=render, bg="red")
        img.image = render
        xCoord = ((256 - opponent.size[0]) / 2)
        yCoord = ((256 - opponent.size[1]) / 2)
        img.place(x=(1024 - opponent.size[0] - xCoord), y=yCoord)
        pass

    def setBattleSection(self):
        Label(self, text="Character Battle Arena").pack()
        Button(self, text="Start Battle", command=self.startBattle).pack()

    def clientExit(self):
        exit()

    def startBattle(self):
        if self.arena.isReady:
            pass
        else:
            messagebox.showinfo("Warning",
                                "Please make sure there are 2 participants in the arena before starting the battle")

    def createNewPlayer(self):
        secondWindow = Toplevel(self.master)
        CharacterWindow(self, secondWindow)

    def addPlayer(self, character):
        self.addPlayerImage(character.characterName, character.imageLoc)
        self.nameValuePlayer['text'] = character.characterName
        self.classNameValuePlayer['text'] = character.characterClass
        self.strengthValuePlayer['text'] = character.strength
        self.quicknessValuePlayer['text'] = character.quickness
        self.healthValuePlayer['text'] = character.health
        self.armorValuePlayer['text'] = character.armor

    def addOpponent(self, opponent):
        self.addOpponentImage(opponent.characterName, opponent.imageLoc)
