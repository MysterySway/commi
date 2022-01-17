import pygam
import sys

class player:
    def __init__(self):
        x,y = (width/2,height/2)
        self.image = pygame.image.load('player.png')
        self.rect