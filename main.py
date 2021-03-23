import pygame 
import numpy as np
from PIL import Image
from EditorUtils import Pixel as p
pygame.init()

class Pixel:
    def __init__(self,x,y):
        self.pixel = pygame.Rect(x, y, block,block)
    def get_pix(self):
        return self.pixel

pixels = []

#sorting image into 100,100,3 array
im = Image.open('image.png')
na = np.array(im)

#defining resolution
x_l = len(na[0])
y_l = len(na)
aspect_ratio = int(x_l/y_l)
x_res = 600
block = x_res/x_l

#creating window
surface = pygame.display.set_mode((x_res,int(x_res/aspect_ratio))) 
color = (255,0,0) 
running = True

#going through each pixel of the image and creating a pixel for it using the pixel class
for x in range(x_l):
    for y in range(y_l):
        pixels.append(p(x, y, block).get_pix())

#drawing wach of the pixel in the list of pixels
for p in pixels:
    pygame.draw.rect(surface,color,p) 

#main GameLoop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.display.flip()