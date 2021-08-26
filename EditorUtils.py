import pygame
from tkinter import *
from tkinter import filedialog

def get_image_file():
    tk=Tk()
    file = filedialog.askopenfilename()
    tk.destroy()
    return file

class Pixel:
    def __init__(self,x,y,block,color):
        self.pixel = pygame.Rect(x* block, y* block, block,block)
        self.color = color
    def get_pix(self):
        return self.pixel
    def get_color(self):
        return self.color

def get_window_resolution(x_l, y_l,greater, screenw, screenh):
    xres : int
    if x_l <= screenh and y_l <= screenw:
        if x_l == y_l:
            if x_l <= 300 and x_l > 150:
                xres = 2*x_l
            else:
                if x_l <= 150 and x_l > 100:
                    xres = 4*x_l
                if x_l < 100:
                    xres = 6*x_l
                else :xres = x_l
        else:
            if greater < 300 and greater > 150:
                xres = 2*greater
            else:
                if greater <= 150 and greater > 100:
                    xres = 4*greater
                elif greater < 100:
                    xres = 6*greater
                else :xres = greater
    else:
        print("cannot open images bigger than the open u have given")
        xres = 0
    return xres
