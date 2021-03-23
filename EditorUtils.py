import pygame
class Pixel:
    def __init__(self,x,y,block,color):
        self.pixel = pygame.Rect(x  * block, y * block, block,block)
        self.color = color
    def get_pix(self):
        return self.pixel
    def get_color(self):
        return self.color