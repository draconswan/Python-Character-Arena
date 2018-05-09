"""

used from: http://effbot.org/zone/tkinter-autoscrollbar.htm
modified from https://stackoverflow.com/questions/41095385/autohide-tkinter-canvas-scrollbar-with-pack-geometry
"""
from tkinter import *


class AutoScrollbar(Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.pack_forget()
        else:
            if self.cget("orient") == HORIZONTAL:
                self.pack(fill=X, side=RIGHT, expand=FALSE)
            else:
                self.pack(fill=Y, side=RIGHT, expand=FALSE)
        Scrollbar.set(self, lo, hi)

    def grid(self, **kw):
        raise TclError("cannot use grid with this widget")

    def place(self, **kw):
        raise TclError("cannot use place with this widget")
