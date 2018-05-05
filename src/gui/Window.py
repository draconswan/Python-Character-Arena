"""

"""
import os
from tkinter import *
from functools import partial
from PIL import Image, ImageTk
from gui.CharacterWindow import CharacterWindow

maxSize = 256, 256


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Character Battle Arena")
        self.pack(fill=BOTH, expand=1)
        self.buildMenu()
        self.showText()
    
    def buildMenu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        players = Menu(file)
        players.add_command(label="Create New", command=self.createNewPlayer)
        players.add_command(label="Fighter", command=partial(self.addPlayer, "fighter"))
        file.add_cascade(label="Add Player", menu=players)
        opponents = Menu(file)
        opponents.add_command(label="Goblin", command=partial(self.addOpponent, "goblin"))
        opponents.add_command(label="Ogre", command=partial(self.addOpponent, "ogre"))
        opponents.add_command(label="Giant", command=partial(self.addOpponent, "giant"))
        file.add_cascade(label="Add Opponent", menu=opponents)
        file.add_command(label="Exit", command=self.clientExit)
        menu.add_cascade(label="File", menu=file)
    
    def addPlayerImage(self, characterName):
        imagePath = "images/" + characterName + ".jpg"
        if os.path.exists(imagePath):
            character = Image.open(imagePath)
        else:
            character = Image.open("images/default.jpg")
        
        character.thumbnail(maxSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(character)
        
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        pass
    
    def addOpponentImage(self, opponentName):
        imagePath = "images/" + opponentName + ".jpg"
        if os.path.exists(imagePath):
            opponent = Image.open(imagePath)
        else:
            opponent = Image.open("images/default.jpg")
        
        opponent.thumbnail(maxSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(opponent)
        
        img = Label(self, image=render)
        img.image = render
        img.place(x=(1024 - opponent.size[0]), y=0)
        pass
    
    def showText(self):
        text = Label(self, text="Character Battle Arena")
        text.pack()
    
    def clientExit(self):
        exit()
        
    def createNewPlayer(self):
        secondWindow = Toplevel(root)
        CharacterWindow(secondWindow)
    
    def addPlayer(self, characterName="fighter"):
        self.addPlayerImage(characterName)
        
        nameLabel = Label(self, text="First Name").grid(row=1)
        nameValue = Label(self, text="Fighter").grid(row=1, column=1)
        
        classNameLabel = Label(self, text="Last Name").grid(row=2)
        classNameValue = Label(self, text="Fighter").grid(row=2, column=1)
        
        strengthLabel = Label(self, text="Strength").grid(row=3)
        strengthValue = Label(self, text="5").grid(row=3, column=1)
        
        quicknessLabel = Label(self, text="Quickness").grid(row=4)
        quicknessValue = Label(self, text="5").grid(row=4, column=1)
        
        healthLabel = Label(self, text="Health").grid(row=5)
        healthValue = Label(self, text="30").grid(row=5, column=1)
        
        armorLabel = Label(self, text="Armor").grid(row=6)
        armorValue = Label(self, text="16").grid(row=6, column=1)
    
    def addOpponent(self, opponentName="goblin"):
        nameLabel = Label(self, text="First Name").grid(row=0)
        nameValue = Label(self, text="Goblin").grid(row=0, column=1)
        
        classNameLabel = Label(self, text="Last Name").grid(row=1)
        classNameValue = Label(self, text="Warrior").grid(row=1, column=1)
        
        strengthLabel = Label(self, text="Strength").grid(row=2)
        strengthValue = Label(self, text="5").grid(row=2, column=1)
        
        quicknessLabel = Label(self, text="Quickness").grid(row=3)
        quicknessValue = Label(self, text="5").grid(row=3, column=1)
        
        healthLabel = Label(self, text="Health").grid(row=4)
        healthValue = Label(self, text="30").grid(row=4, column=1)
        
        armorLabel = Label(self, text="Armor").grid(row=5)
        armorValue = Label(self, text="14").grid(row=5, column=1)
        
        self.addOpponentImage(opponentName)


root = Tk()

root.geometry("1024x768")

app = Window(root)
root.mainloop()
