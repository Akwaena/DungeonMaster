from Data.Items.Armor import *
from Data.Items.Weapons import *
from Data.Items.Artifacts import *
from Tools.debugger import *
from random import randint, shuffle
import pygame as game
from pygame.locals import *


class Dungeon:
    def __init__(self, run_num):
        self.available_loot = [[i for i in weapons if i.lvl == run_num],
                               [i for i in armor if i.lvl == run_num],
                               [i for i in artifacts if i.lvl == run_num]]
        self.run = run_num
        self.rooms = []

    def create(self):
        log('DungeonGenerator/Генерируется подземелье')
        room_num = randint(10, 15)
        first_room_y = randint(0, 10)
        counter = 1
        insides = ['loot', 'enemy', 'empty', 'loot', 'enemy', 'empty', 'loot', 'enemy', 'empty', 'trap']
        self.rooms.append(Room(0, (0, first_room_y), 'enter'))
        while room_num:
            split_type = randint(1, 2)
            log(f'DungeonGenerator/Идет генерация. Семя шага {split_type}.{room_num}')
            if room_num == 1:
                self.rooms.append(Room(counter, (self.rooms[counter - 1].x + 1, abs(first_room_y + randint(-3, 3))),
                                       'exit'))
                self.rooms[-1].connect(self.rooms[-2])
                log('DungeonGenerator/Генерация завершена')
                break
            if split_type == 1:
                log('DungeonGenerator/Выбран прямой путь')
                shuffle(insides)
                self.rooms.append(Room(counter, (self.rooms[counter - 1].x + 1, abs(first_room_y + randint(-3, 3))),
                                       insides[0]))
                self.rooms[-1].connect(self.rooms[-2])
            if split_type == 2:
                log('DungeonGenerator/Выбрана развилка')
                shuffle(insides)
                if randint(0, 1) == 1:
                    self.rooms.append(Room(counter, (self.rooms[counter - 1].x + 1, abs(first_room_y + randint(-3, 3))),
                                           insides[0]))
                    self.rooms.append(Room(counter + 1, (self.rooms[counter - 1].x + 1,
                                                         abs(first_room_y + randint(-3, 3))), insides[0]))
                else:
                    self.rooms.append(Room(counter, (self.rooms[counter - 1].x + 1,
                                                     abs(first_room_y + randint(-3, 3))), insides[0]))
                    self.rooms.append(Room(counter + 1, (self.rooms[counter - 1].x + 1,
                                                         abs(first_room_y + randint(-3, 3))), insides[0]))
                self.rooms[-1].connect(self.rooms[-3])
                self.rooms[-2].connect(self.rooms[-3])
            room_num -= 1
            counter += 1
        log(f'DungeonGenerator/Результат генерации:')
        for i in self.rooms:
            log(f'DungeonGenerator/{i}')

    def render(self, screen, icons, left=1, top=1, mod=50, con_color=(255, 255, 255), con_width=1):
        log('DungeonGenerator/Рендер комнат')
        for i in self.rooms:
            if i.inside == 'enemy':
                icon = icons[0]
                icon.rect.x = (left + i.x) * mod
                icon.rect.y = (top + i.y) * mod
                log(f'DungeonGenerator/Рисуется враг ({i.x * mod}, {i.y * mod})')
            elif i.inside == 'loot':
                icon = icons[1]
                icon.rect.x = (left + i.x) * mod
                icon.rect.y = (top + i.y) * mod
                log(f'DungeonGenerator/Рисуется лут ({i.x * mod}, {i.y * mod})')
            elif i.inside == 'trap':
                icon = icons[3]
                icon.rect.x = (left + i.x) * mod
                icon.rect.y = (top + i.y) * mod
                log(f'DungeonGenerator/Рисуется ловушка ({i.x * mod}, {i.y * mod})')
            elif i.inside == 'enter':
                icon = icons[4]
                icon.rect.x = (left + i.x) * mod
                icon.rect.y = (top + i.y) * mod
                log(f'DungeonGenerator/Рисуется выход ({i.x * mod}, {i.y * mod})')
            elif i.inside == 'exit':
                icon = icons[5]
                icon.rect.x = (left + i.x) * mod
                icon.rect.y = (top + i.y) * mod
                log(f'DungeonGenerator/Рисуется выход ({i.x * mod}, {i.y * mod})')
            elif i.inside == 'empty':
                icon = icons[2]
                icon.rect.x = (left + i.x) * mod
                icon.rect.y = (top + i.y) * mod
                log(f'DungeonGenerator/Рисуется пустая комната ({i.x * mod}, {i.y * mod})')
            else:
                log('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                log(f'Ошибка! DungeonGenerator, строка 93; Некорректное содержимое комнаты {i.id}')
                log('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                icon = None
                exit(1)
            screen.blit(icon.image, icon.rect)

        log('DungeonGenerator/Рендер соединений')
        for room in self.rooms:
            print('____________________________________________')
            print('хост')
            print(room)
            connected = room.connected
            while connected:
                con = connected.pop()
                print('клиент')
                print(con)
                game.draw.line(screen, con_color, ((left + room.x) * mod, (top + room.y) * mod),
                               ((left + con.x) * mod, (top + con.y * mod)), con_width)
            print('____________________________________________')

    def visual_test(self):
        RESOLUTION = (1280, 720)
        FPS = 1
        screen = game.display.set_mode(RESOLUTION)
        game.display.set_caption('Тест генерации уровня')
        BLACK = (0, 0, 0)

        game.time.Clock().tick(FPS)
        screen.fill(BLACK)
        icons = []
        enemy = game.image.load('Tools/gen_test_enemy.png')
        enemy_sprite = game.sprite.Sprite()
        enemy_sprite.image = enemy
        enemy_sprite.rect = enemy_sprite.image.get_rect()
        icons.append(enemy_sprite)
        loot = game.image.load('Tools/gen_test_loot.png')
        loot_sprite = game.sprite.Sprite()
        loot_sprite.image = loot
        loot_sprite.rect = loot_sprite.image.get_rect()
        icons.append(loot_sprite)
        empty = game.image.load('Tools/gen_test_nothing.png')
        empty_sprite = game.sprite.Sprite()
        empty_sprite.image = empty
        empty_sprite.rect = empty_sprite.image.get_rect()
        icons.append(empty_sprite)
        trap = game.image.load('Tools/gen_test_trap.png')
        trap_sprite = game.sprite.Sprite()
        trap_sprite.image = trap
        trap_sprite.rect = trap_sprite.image.get_rect()
        icons.append(trap_sprite)
        enter = game.image.load('Tools/gen_test_enter.png')
        enter_sprite = game.sprite.Sprite()
        enter_sprite.image = enter
        enter_sprite.rect = enter_sprite.image.get_rect()
        icons.append(enter_sprite)
        ext = game.image.load('Tools/gen_test_enter.png')
        ext_sprite = game.sprite.Sprite()
        ext_sprite.image = ext
        ext_sprite.rect = ext_sprite.image.get_rect()
        icons.append(ext_sprite)
        self.render(screen, icons)
        game.display.update()
        n = input()


class Room:
    def __init__(self, r_id, coord, inside):
        self.id = r_id
        self.x = coord[0]
        self.y = coord[1]
        self.inside = inside
        self.connected = []

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        returned = ''
        for i in self.connected:
            returned += f'[id={i.id} ({i.x} {i.y})] '
        return f'Комната {self.id}, ({self.x}, {self.y}), соединена с {returned}, внутри {self.inside}'

    def connect(self, other):
        for i in self.connected:
            if i == other:
                return
        self.connected.append(other)
        other.connected.append(self)
        log(f'DungeonGenerator/Подключена ячейка {other.id} к {self.id}')

    def disconnect(self, other):
        for i in range(len(self.connected)):
            if self.connected[i] == other:
                for j in range(len(other.connected)):
                    if other.connected[j] == self.connected[i]:
                        log(f'DungeonGenerator/Отключена ячейка {other.id} от {self.id}')
                        del other.connected[j]
                        del self.connected[i]

    def insert(self, item):
        self.inside = item

    def interact(self):
        pass

    def move(self):
        pass


dung = Dungeon(1)
dung.create()
dung.visual_test()
