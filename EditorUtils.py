import pygame
class Pixel:
    def __init__(self,x,y,block,color):
        self.pixel = pygame.Rect(x* block, y* block, block,block)
        self.color = color
    def get_pix(self):
        return self.pixel
    def get_color(self):
        return self.color

def get_window_resolution(x_l, y_l,greater):
    xres : int
    if x_l == y_l:
        if x_l <= 300:
            xres = 2*x_l
        else:
            xres = x_l
    else:
        if greater < 300:
            xres = 2*greater
        else:
            xres = greater
    return xres