import pygame as game
from pygame.locals import *


class Dot:
    def __init__(self, coord):
        self.coord = coord

    def __eq__(self, other):
        return other.collidepoint(self.coord)

def collide_button(buttons, dot):
    for i in
