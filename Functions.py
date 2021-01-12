import pygame as game
from pygame.locals import *


class Dot:
    def __init__(self, coord):
        self.coord = coord

    def __eq__(self, other):
        return self.coord == other.coord


class Button:
    def __init__(self, rect, name, function=None):
        self.rect = rect
        self.name = name
        if function:
            self.function = function

    def __eq__(self, other):
        if not other:
            return False
        return self.name == other.name

    def connect(self, function):
        self.function = function


def collide_button(buttons, dot):
    for i in buttons:
        if i.rect.collidepoint(dot.coord):
            return i
    return False


class Game:
    def __init__(self):
        pass


class FamilyMember:
    def __init__(self):
        pass


class Hero:
    def __init__(self):
        pass


class Dungeon:
    def __init__(self):
        pass


class Room:
    def __init__(self):
        pass
