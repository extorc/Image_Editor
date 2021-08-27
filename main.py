import pygame
import numpy as np
import PIL.Image
import EditorUtils as e
import time

im = PIL.Image.open(e.get_image_file())
na = np.array(im)

pygame.init()
pixels = []

#sorting image into 100,100,3 array


#defining resolution
monitor = pygame.display.Info()
screenw = monitor.current_w
screenh = monitor.current_h

x_l = len(na[0])
y_l = len(na)
greater = max(x_l, y_l)
x_res = e.get_window_resolution(x_l, y_l, greater, screenw, screenh)
print(x_res)
if x_res == 0:
    exit()
aspect_ratio = (x_l/y_l)
block = x_res/greater

#creating window
surface = pygame.display.set_mode((x_res,int(x_res/aspect_ratio)))
color = (255,0,0)
running = True

#going through each pixel of the image and creating a pixel for it using the pixel class
for x in range(x_l):
    for y in range(y_l):
        pixels.append(e.Pixel(x, y, block,na[y][x].tolist()))

#drawing each of the pixel in the list of pixels
for p in pixels:
    pygame.draw.rect(surface,p.get_color(),p.get_pix())
n = 0
#main GameLoop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if n <= 30:
        for p in pixels:
            pygame.draw.rect(surface,p.get_color(),p.get_pix())
    else:
        for p in pixels:
            p.set_color([100,100,100])
            pygame.draw.rect(surface,p.get_color(),p.get_pix())
    n += 1
    print(n)
    pygame.display.update()
pygame.display.flip()
