import pygame
class Pixel:
    def __init__(self,x,y,block):
        self.pixel = pygame.Rect(x  * block, y * block, block,block)
    def get_pix(self):
        return self.pixel