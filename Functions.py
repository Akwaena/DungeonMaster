import pygame as game
from pygame.locals import *
import sqlite3 as sql
from Tools.debugger import *


class Dot:
    def __init__(self, coord):
        self.coord = coord

    def __eq__(self, other):
        return self.coord == other.coord


class Button:
    def __init__(self, sprite, name, function=None, text=None):
        self.rect = sprite.rect
        self.image = sprite.image
        self.name = name
        self.text = text
        if function:
            self.function = function

    def __eq__(self, other):
        if not other:
            return False
        return self.name == other.name

    def __str__(self):
        return f'{self.name}: {self.rect}; {self.text}'

    def connect(self, function):
        self.function = function

    def render(self, screen):
        screen.blit(self.image, self.rect)


def collide_button(buttons, dot):
    for i in buttons:
        if i.rect.collidepoint(dot.coord):
            return i
    return False


class Save:
    def __init__(self):
        self.con = sql.connect('Data/save.db')
        self.cur = self.con.cursor()
        log('Functions/Инициализировано сохранение')

        self.raids = None
        self.hope = None
        self.xp = None
        self.all_xp = None
        self.skills = None
        self.weapon = None
        self.all_weapon = None
        self.armor = None
        self.all_armor = None
        self.artifact = None
        self.all_artifact = None
        self.stock_food = None
        self.pocket_food = None
        self.father = None
        self.mother = None
        self.granddad = None
        self.elder_sis = None
        self.younger_sis = None
        self.maid = None
        self.guest = None
        self.cat = None
        self.all_consumption = 0
        self.family = None
        self.events = None

    def load(self):
        self.raids = self.cur.execute('''SELECT raids FROM save''').fetchone()[0]
        self.hope = self.cur.execute('''SELECT hope FROM save''').fetchone()[0]
        self.xp = self.cur.execute('''SELECT xp FROM save''').fetchone()[0]
        self.all_xp = self.cur.execute('''SELECT all_xp FROM save''').fetchone()[0]
        self.skills = self.cur.execute('''SELECT skills FROM save''').fetchone()[0]
        self.weapon = self.cur.execute('''SELECT weapon FROM save''').fetchone()[0]
        self.all_weapon = self.cur.execute('''SELECT all_weapon FROM save''').fetchone()[0]
        self.armor = self.cur.execute('''SELECT armor FROM save''').fetchone()[0]
        self.all_armor = self.cur.execute('''SELECT all_armor FROM save''').fetchone()[0]
        self.artifact = self.cur.execute('''SELECT artifact FROM save''').fetchone()[0]
        self.all_artifact = self.cur.execute('''SELECT all_artifact FROM save''').fetchone()[0]
        self.stock_food = self.cur.execute('''SELECT stock_food FROM save''').fetchone()[0]
        self.pocket_food = self.cur.execute('''SELECT pocket_food FROM save''').fetchone()[0]

        self.father = self.cur.execute('''SELECT father FROM save''').fetchone()[0]
        self.mother = self.cur.execute('''SELECT mother FROM save''').fetchone()[0]
        self.granddad = self.cur.execute('''SELECT granddad FROM save''').fetchone()[0]
        self.elder_sis = self.cur.execute('''SELECT elder_sis FROM save''').fetchone()[0]
        self.younger_sis = self.cur.execute('''SELECT younger_sis FROM save''').fetchone()[0]
        self.maid = self.cur.execute('''SELECT maid FROM save''').fetchone()[0]
        self.guest = self.cur.execute('''SELECT guest FROM save''').fetchone()[0]
        self.cat = self.cur.execute('''SELECT cat FROM save''').fetchone()[0]

        self.events = self.cur.execute('''SELECT events FROM save''').fetchone()[0]

        self.family = (FamilyMember('Отец', 'Male', Buff('атака', 10), self.father),
                       FamilyMember('Мать', 'Female', Buff('еда с вылазок', 10), self.mother),
                       FamilyMember('Дед', 'Male', Buff('опыт', 50), self.granddad),
                       FamilyMember('Старшая сестра', 'Female', Buff('здоровье', 10), self.elder_sis),
                       FamilyMember('Младшая сестра', 'Female', alive=self.younger_sis),
                       FamilyMember('Служанка', 'Female', Buff('еда с вылазки', 5), self.maid),
                       FamilyMember('Гость', 'Male', alive=self.guest),
                       FamilyMember('Кот', 'Male', alive=self.cat, food_consumption=1))

        for i in self.family:
            self.all_consumption += i.food_consumption

        log('Functions/Загружено сохранение')

    def save(self):
        self.cur.execute(f'''UPDATE save SET raids = {self.raids}''')
        self.cur.execute(f'''UPDATE save SET hope = {self.hope}''')
        self.cur.execute(f'''UPDATE save SET xp = {self.xp}''')
        self.cur.execute(f'''UPDATE save SET all_xp = {self.all_xp}''')
        self.cur.execute(f'''UPDATE save SET skills = "{self.skills}"''')
        self.cur.execute(f'''UPDATE save SET weapon = {self.weapon}''')
        self.cur.execute(f'''UPDATE save SET all_weapon = "{self.all_weapon}"''')
        self.cur.execute(f'''UPDATE save SET armor = {self.armor}''')
        self.cur.execute(f'''UPDATE save SET all_armor = "{self.armor}"''')
        self.cur.execute(f'''UPDATE save SET artifact = {self.artifact}''')
        self.cur.execute(f'''UPDATE save SET all_artifact = "{self.all_artifact}"''')
        self.cur.execute(f'''UPDATE save SET stock_food = {self.stock_food}''')
        self.cur.execute(f'''UPDATE save SET pocket_food = {self.pocket_food}''')
        self.cur.execute(f'''UPDATE save SET father = {self.father}''')
        self.cur.execute(f'''UPDATE save SET mother = {self.mother}''')
        self.cur.execute(f'''UPDATE save SET granddad = {self.granddad}''')
        self.cur.execute(f'''UPDATE save SET elder_sis = {self.elder_sis}''')
        self.cur.execute(f'''UPDATE save SET younger_sis = {self.younger_sis}''')
        self.cur.execute(f'''UPDATE save SET maid = {self.maid}''')
        self.cur.execute(f'''UPDATE save SET guest = {self.guest}''')
        self.cur.execute(f'''UPDATE save SET cat = {self.cat}''')

        self.cur.execute(f'''UPDATE save SET events = "{self.events}"''')
        self.con.commit()

        log('Functions/Игра сохранена')

    def clear(self):
        self.cur.execute('''DELETE FROM save''')
        # Костыль для создания новой строки
        self.cur.execute('''INSERT INTO save (father) VALUES (True)''')


class Game:
    def __init__(self):
        pass


class FamilyMember:
    def __init__(self, name, sex, buff=None, alive=True, food_consumption=3):
        self.name = name
        self.buff = buff
        self.sex = sex
        self.alive = alive
        self.food_consumption = food_consumption

        if not alive:
            self.food_consumption = 0

    def kill(self):
        self.alive = False
        self.food_consumption = 0
        self.buff = None

    def render(self, screen, font, y):
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        screen.blit(font.render(f'{self.name} - {self.status()}', True, WHITE), Rect(30, y, 500, 45))
        if self.buff:
            screen.blit(font.render(f'+{self.buff}', True, GREEN), Rect(500, y, 500, 45))
        screen.blit(font.render(f'-{self.food_consumption}еды/день', True, RED), Rect(850, y, 500, 45))

    def status(self):
        if self.alive:
            if self.sex == 'Male':
                return 'жив'
            else:
                return 'жива'
        else:
            if self.sex == 'Female':
                return 'мертва'
            else:
                return 'мертв'


class Buff:
    def __init__(self, perk, strength):
        self.perk = perk
        self.strength = strength

    def __str__(self):
        return f'{self.strength}% {self.perk}'


class Hero:
    def __init__(self, start_pos, save):
        pass
