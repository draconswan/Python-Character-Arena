"""
Created on 5/2/18

@author:   Daniel Swan & Erin Swan
@email:    ds235410@my.stchas.edu & es209931@my.stchas.edu
"""
from functools import *
from tkinter import *
from classes.Character import Character


class CharacterWindow(Frame):
    
    # When a player chooses to create their own character, a new instance of CharacterWindow
    # containing a main window and a master frame of None is created by calling the init_window method
    def __init__(self, mainWindow, master=None):
        Frame.__init__(self, master)
        self.mainWindow = mainWindow
        self.master = master
        self.init_window()

    # Creates the pop up window that the user will use to create their own character
    def init_window(self):
        self.master.title("Character Creation")
        self.pack(fill=BOTH, expand=1)
        
        # Creates a text box for character name in a specified location and tells the user the
        # parameters of their input, which is validated when they attempt to create the new character
        Label(self, text="Character Name").grid(row=0)
        self.name = Entry(self)
        self.name.grid(row=0, column=1)
        self.nameMessage = Label(self, text="Please enter 1-20 characters")
        self.nameMessage.grid(row=0, column=2)

        # Creates a drop-down list of character classes that the user may choose from. Currently, it's a static list
        Label(self, text="Character Class").grid(row=1)
        self.className = StringVar(self)
        classList = ["Fighter", "Brawler", "Mage", "Rogue", "Cleric"]
        self.className.set(classList[0])
        self.classNameOption = OptionMenu(self, self.className, *classList)
        self.classNameOption.grid(row=1, column=1)

        # Creates a text box for character strength in a specified location and tells the user the
        # parameters of their input, which is validated when they attempt to create the new character
        Label(self, text="Strength").grid(row=2)
        self.strength = Entry(self)
        self.strength.grid(row=2, column=1)
        self.strength.insert(10, 5)
        self.strengthMessage = Label(self, text="Please enter a number between 1 and 20")
        self.strengthMessage.grid(row=2, column=2)

        # Creates a text box for character quickness in a specified location and tells the user the
        # parameters of their input, which is validated when they attempt to create the new character
        Label(self, text="Quickness").grid(row=3)
        self.quickness = Entry(self)
        self.quickness.grid(row=3, column=1)
        self.quickness.insert(10, 5)
        self.quicknessMessage = Label(self, text="Please enter a number between 1 and 20")
        self.quicknessMessage.grid(row=3, column=2)

        # Creates a text box for character health in a specified location and tells the user the
        # parameters of their input, which is validated when they attempt to create the new character
        Label(self, text="Health").grid(row=4)
        self.health = Entry(self)
        self.health.grid(row=4, column=1)
        self.health.insert(10, 30)
        self.healthMessage = Label(self, text="Please enter a number between 1 and 200")
        self.healthMessage.grid(row=4, column=2)

        # Creates a text box for character armor in a specified location and tells the user the
        # parameters of their input, which is validated when they attempt to create the new character
        Label(self, text="Armor").grid(row=5)
        self.armor = Entry(self)
        self.armor.grid(row=5, column=1)
        self.armor.insert(10, 16)
        self.armorMessage = Label(self, text="Please enter a number between 1 and 30")
        self.armorMessage.grid(row=5, column=2)

        # creates a button that allows the user to exit out of the character creation window
        self.cancelButton = Button(self, text="Cancel", command=self.master.destroy)
        self.cancelButton.grid(row=6, column=0, sticky=W, pady=4)
        self.createButton = Button(self, text="Create", command=partial(self.create))
        self.createButton.grid(row=6, column=1, sticky=W, pady=4)

    # Instantiates a new character class and validates all of the user inputs
    # If any input check fails, the offending user guide label text is updated from black to red
    # to call attention to the check that failed to meet the specified input criteria
    def create(self):
        valid = True
        player = Character()
        nameInput = self.name.get()
        # Input validation for the Character Name
        if len(nameInput) < 1 or len(nameInput) > 20:
            valid = False
            self.nameMessage['fg'] = "red"
        else:
            self.nameMessage['fg'] = "black"
            player.characterName = nameInput
        player.characterClass = self.className.get()
        # Input validation for the Character strength
        try:
            strengthInput = int(self.strength.get())
            if strengthInput < 1 or strengthInput > 20:
                raise ValueError("Value out of range")
            else:
                self.strengthMessage['fg'] = "black"
                player.strength = strengthInput
        except (TypeError, ValueError):
            valid = False
            self.strengthMessage['fg'] = "red"
        # Input validation for the Character quickness
        try:
            quicknessInput = int(self.quickness.get())
            if quicknessInput < 1 or quicknessInput > 20:
                raise ValueError("Value out of range")
            else:
                self.quicknessMessage['fg'] = "black"
                player.quickness = quicknessInput
        except (TypeError, ValueError):
            valid = False
            self.quicknessMessage['fg'] = "red"
        # Input validation for the Character health
        try:
            healthInput = int(self.health.get())
            if healthInput < 1 or healthInput > 200:
                raise ValueError("Value out of range")
            else:
                self.healthMessage['fg'] = "black"
                player.health = healthInput
        except (TypeError, ValueError):
            valid = False
            self.healthMessage['fg'] = "red"
        # Input validation for the Character armor
        try:
            armorInput = int(self.armor.get())
            if armorInput < 1 or armorInput > 30:
                raise ValueError("Value out of range")
            else:
                self.armorMessage['fg'] = "black"
                player.armor = armorInput
        except (TypeError, ValueError):
            valid = False
            self.armorMessage['fg'] = "red"
        # If all input test has been passed, populate the player information in the master window
        # and close the pop-up character input window
        if valid:
            self.mainWindow.addPlayer(player)
            self.master.destroy()
