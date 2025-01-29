import tkinter
import random  

ROWS = 25
COLS = 50
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS #25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS #25*25 = 625

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window
window = tkinter.Tk()
window.title("TyrannoSeahorse Rex Evolvee")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()
