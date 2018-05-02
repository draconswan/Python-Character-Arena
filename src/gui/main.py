"""

"""
from tkinter import *
from PIL import Image, ImageTk

maxSize = 256, 256


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.showText()

    def init_window(self):
        self.master.title("Character Battle Arena")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Add Player", command=self.addPlayer)
        file.add_command(label="Add Opponent", command=self.addOpponent)
        file.add_command(label="Exit", command=self.clientExit)
        menu.add_cascade(label="File", menu=file)

    def addPlayerImage(self):
        fighter = Image.open("images/fighter.jpg")
        fighter.thumbnail(maxSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(fighter)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def addOpponentImage(self):
        goblin = Image.open("images/goblin.jpg")
        goblin.thumbnail(maxSize, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(goblin)

        img = Label(self, image=render)
        img.image = render
        img.place(x=(1024 - goblin.size[0]), y=0)

    def showText(self):
        text = Label(self, text="Hey listen!")
        text.pack()

    def clientExit(self):
        exit()

    def addPlayer(self):
        self.addPlayerImage()

    def addOpponent(self):
        self.addOpponentImage()


root = Tk()

root.geometry("1024x768")

app = Window(root)
root.mainloop()
