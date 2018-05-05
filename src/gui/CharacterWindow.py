"""

"""
import atexit
from functools import *
from tkinter import *
from classes.Character import Character
from classes.Arena import Arena


class CharacterWindow(Frame):

    def __init__(self, mainWindow, master=None):
        Frame.__init__(self, master)
        self.mainWindow = mainWindow
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Character Creation")
        self.pack(fill=BOTH, expand=1)

        Label(self, text="Character Name").grid(row=0)
        self.name = Entry(self)
        self.name.grid(row=0, column=1)

        Label(self, text="Character Class").grid(row=1)
        self.className = StringVar(self)
        classList = ["Fighter", "Knight", "Mage", "Rogue"]
        self.className.set(classList[0])
        self.classNameOption = OptionMenu(self, self.className, *classList)
        self.classNameOption.grid(row=1, column=1)

        Label(self, text="Strength").grid(row=2)
        self.strength = Entry(self)
        self.strength.grid(row=2, column=1)
        self.strength.insert(10, 5)

        Label(self, text="Quickness").grid(row=3)
        self.quickness = Entry(self)
        self.quickness.grid(row=3, column=1)
        self.quickness.insert(10, 5)

        Label(self, text="Health").grid(row=4)
        self.health = Entry(self)
        self.health.grid(row=4, column=1)
        self.health.insert(10, 30)

        Label(self, text="Armor").grid(row=5)
        self.armor = Entry(self)
        self.armor.grid(row=5, column=1)
        self.armor.insert(10, 16)

        self.cancelButton = Button(self, text="Cancel", command=self.master.destroy)
        self.cancelButton.grid(row=6, column=0, sticky=W, pady=4)
        self.createButton = Button(self, text="Create", command=partial(self.create))
        self.createButton.grid(row=6, column=1, sticky=W, pady=4)

    def create(self):
        player = Character()
        player.characterName = self.name.get()
        player.characterClass = self.className.get()
        player.strength = int(self.strength.get())
        player.quickness = int(self.quickness.get())
        player.health = int(self.health.get())
        player.armor = int(self.armor.get())
        print(player)
        self.mainWindow.addPlayer(player)
        self.master.destroy()
