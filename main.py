import pygame 
import numpy as np
import PIL.Image
from EditorUtils import Pixel as p
from EditorUtils import *
from tkinter import *
from tkinter import filedialog

tk=Tk()
file = filedialog.askopenfilename()
tk.destroy()
im = PIL.Image.open(file)
na = np.array(im)

pygame.init()
pixels = []

#sorting image into 100,100,3 array


#defining resolution
x_l = len(na[0])
y_l = len(na)
greater = max(x_l, y_l)
x_res = get_window_resolution(x_l, y_l, greater)
aspect_ratio = (x_l/y_l)
block = x_res/x_l

#creating window
surface = pygame.display.set_mode((x_res,int(x_res/aspect_ratio))) 
color = (255,0,0) 
running = True

#going through each pixel of the image and creating a pixel for it using the pixel class
for x in range(x_l):
    for y in range(y_l):
        pixels.append(p(x, y, block,na[y][x].tolist()))

#drawing each of the pixel in the list of pixels
for p in pixels:
    pygame.draw.rect(surface,p.get_color(),p.get_pix()) 

#main GameLoop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.display.flip()