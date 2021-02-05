from random import randint


class Hero:
    """Герой"""
    def __init__(self, starting_room):
        self.hp = 100
        self.room = starting_room
        self.rail = 1


class Monster:
    """Враг"""
    def __init__(self):
        self.hp = randint(20, 50)
        self.dmg = randint(10, 50)
        self.rail = 1

    def switch(self):
        self.rail = randint(0, 2)
