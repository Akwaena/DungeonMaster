import pygame as game
from pygame.locals import *

from config_parser import *
from buttons import *

import dungeon_generator
from character import *

from random import randint

# импорт сохраненной информации
config = parse_txt('config', 'config.txt')
max_score = parse_txt('score', 'score.txt')

# Создание экрана
screen = game.display.set_mode(format_resolution(config['RESOLUTION']))
game.display.set_caption('Мастер Подземелий')

# Создание игровых объектов
dungeon = dungeon_generator.Dungeon()
dungeon.generate(randint(7, 15))
hero = Hero(dungeon[0])
enemy = None
score = 0

# Создание цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (60, 100, 50)
BLUE = (0, 0, 255)
BROWN = (70, 50, 30)
YELLOW = (255, 243, 67)

# Списки со спрайтами
menu_sprites = []
menu_buttons = []
dungeon_sprites = []
icons = []

# Создание основных переменных
layout = 'main_menu'
game_status = 'normal'
level_counter = 1

# Шрифты
game.font.init()
font_36 = game.font.Font('Fonts/GothicRus.ttf', 36)


def render():
    """
    Отрисовка кадра
    """
    global layout
    global menu_sprites
    global menu_buttons

    # Лэйаут главного меню
    if layout == 'main_menu':
        for sprite in menu_sprites:
            screen.blit(sprite.image, sprite.rect)

        for i in menu_buttons:
            i.render(screen)
        screen.blit(font_36.render(f'{max_score} монет', True, BLACK), Rect(1300, 700, 650, 150))

    # Лэйаут подземелья
    elif layout == 'dungeon':
        # Экран смерти
        if game_status == 'game_over':
            screen.blit(end_screen.image, end_screen.rect)
            return
        for sprite in dungeon_sprites:
            screen.blit(sprite.image, sprite.rect)

        # Отрисовка игрока
        if hero.rail == 0:
            hero_sprite.rect.x = 1430
        elif hero.rail == 1:
            hero_sprite.rect.x = 1550
        elif hero.rail == 2:
            hero_sprite.rect.x = 1670
        screen.blit(hero_sprite.image, hero_sprite.rect)

        # Отрисовка подземелья
        mod = 100
        dungeon.render(screen, icons, 50, 50, mod)
        hero_room.rect.x = (hero.room.id + 1) * mod + 50
        screen.blit(hero_room.image, hero_room.rect)

        # Отрисовка текстовой информации
        screen.blit(font_36.render(f'{score} монет', True, YELLOW), Rect(50, 50, 500, 500))

        screen.blit(font_36.render('Герой', True, BLACK), Rect(1215, 800, 100, 50))
        screen.blit(font_36.render(f'{hero.hp} HP', True, DARK_GREEN), Rect(1215, 850, 100, 50))

        screen.blit(font_36.render(f'{level_counter} этаж', True, YELLOW), Rect(50, 300, 500, 500))

        # Отрисовка врага, информации о нем
        if in_battle:
            screen.blit(font_36.render('Враг', True, BLACK), Rect(1750, 800, 100, 50))
            screen.blit(font_36.render(f'{enemy.hp} HP', True, RED), Rect(1780, 850, 100, 50))
            screen.blit(font_36.render(f'{enemy.dmg} DMG', True, RED), Rect(1780, 900, 100, 50))

        if enemy:
            if enemy.rail == 0:
                attack_soon.rect.x = 1460
                screen.blit(attack_soon.image, attack_soon.rect)
            else:
                attack_never.rect.x = 1460
                screen.blit(attack_never.image, attack_never.rect)
            if enemy.rail == 1:
                attack_soon.rect.x = 1580
                screen.blit(attack_soon.image, attack_soon.rect)
            else:
                attack_never.rect.x = 1580
                screen.blit(attack_never.image, attack_never.rect)
            if enemy.rail == 2:
                attack_soon.rect.x = 1700
                screen.blit(attack_soon.image, attack_soon.rect)
            else:
                attack_never.rect.x = 1700
                screen.blit(attack_never.image, attack_never.rect)
        else:
            attack_never.rect.x = 1460
            screen.blit(attack_never.image, attack_never.rect)

            attack_soon.rect.x = 1580
            screen.blit(attack_soon.image, attack_soon.rect)

            attack_never.rect.x = 1700
            screen.blit(attack_never.image, attack_never.rect)


def start():
    """
    Старт нового забега
    """
    global layout
    global game_status
    global score
    global level_counter
    global hero
    global dungeon
    global enemy
    global in_battle
    enemy = None
    score = 0
    layout = 'dungeon'
    game_status = 'normal'
    score = 0
    level_counter = 1
    dungeon = dungeon_generator.Dungeon()
    dungeon.generate(randint(7, 15))
    hero = Hero(dungeon[0])
    enemy = None
    in_battle = False


#######################################################################################################################

def dodge(direction):
    """
    Уворот в left или в right
    """
    if direction == 'left':
        if hero.rail > 0:
            hero.rail -= 1
    elif direction == 'right':
        if hero.rail < 2:
            hero.rail += 1


def move(direction):
    """
    Движение по карте в left или в right
    """
    if not in_battle:
        if direction == 'right':
            if len(dungeon.rooms) > hero.room.id + 1:
                hero.room = dungeon.rooms[hero.room.id + 1]
        elif direction == 'left':
            if hero.room.id > 0:
                hero.room = dungeon.rooms[hero.room.id - 1]


def attack():
    """
    Атака по врагу
    """
    global in_battle
    global enemy
    global counter

    if enemy:
        if counter <= 0:
            enemy.hp -= randint(1, 10)
            counter = 30
            if enemy.hp <= 0:
                in_battle = False
                hero.room.inside = 'loot'


def interact():
    """
    Действия с комнатой
    """
    global enemy
    global in_battle
    global hero
    global score
    global level_counter

    if hero.room.inside == 'loot':
        score += 1
        hero.room.inside = 'empty'

    if hero.room.inside == 'enemy':
        if not in_battle:
            enemy = Monster()
            in_battle = True

    if hero.room.inside == 'exit':
        score += 5
        dungeon.generate()
        hero.room = dungeon[0]
        level_counter += 1


# Загрузка спрайтов главного меню
########################################################################################################################
menu_background = game.sprite.Sprite()
menu_background.image = game.image.load('Img/Backgrounds/menu_background.png')
menu_background.rect = Rect(0, 0, 1920, 1080)
menu_sprites.append(menu_background)

record_background = game.sprite.Sprite()
record_background.image = game.image.load('Img/Backgrounds/record_background.png')
record_background.rect = Rect(1270, 630, 650, 150)
menu_sprites.append(record_background)

start_button = game.sprite.Sprite()
start_button.image = game.image.load('Img/Buttons/new_game_button.png')
start_button.rect = Rect(1270, 780, 650, 150)
menu_buttons.append(Button(start_button, game.image.load('Img/Buttons/new_game_button_pressed.png'), start))

exit_button = game.sprite.Sprite()
exit_button.image = game.image.load('Img/Buttons/exit_button.png')
exit_button.rect = Rect(1270, 930, 650, 150)
menu_buttons.append(Button(exit_button, game.image.load('Img/Buttons/exit_button_pressed.png'), exit))

# Загрузка спрайтов подземелья
########################################################################################################################
background = game.sprite.Sprite()
background.image = game.image.load('Img/Backgrounds/dungeon_background.png')
background.rect = Rect(0, 0, 1920, 1080)
dungeon_sprites.append(background)

end_screen = game.sprite.Sprite()
end_screen.image = game.image.load('Img/Backgrounds/death_screen.png')
end_screen.rect = Rect(0, 0, 1920, 1080)

hero_sprite = game.sprite.Sprite()
hero_sprite.image = game.image.load('Img/Dungeon/hero.png')
hero_sprite.rect = Rect(1540, 1020, 100, 50)

hero_room = game.sprite.Sprite()
hero_room.image = game.image.load('Img/Dungeon/hero_room.png')
hero_room.rect = Rect(1580, 550, 50, 50)

empty_room = game.sprite.Sprite()
empty_room.image = game.image.load('Img/Dungeon/empty.png')
empty_room.rect = Rect(1580, 805, 50, 50)
icons.append(empty_room)

enemy_room = game.sprite.Sprite()
enemy_room.image = game.image.load('Img/Dungeon/enemy.png')
enemy_room.rect = Rect(1580, 805, 50, 50)
icons.append(enemy_room)

loot_room = game.sprite.Sprite()
loot_room.image = game.image.load('Img/Dungeon/loot.png')
loot_room.rect = Rect(1580, 805, 50, 50)
icons.append(loot_room)

enter_room = game.sprite.Sprite()
enter_room.image = game.image.load('Img/Dungeon/enter.png')
enter_room.rect = Rect(1580, 805, 50, 50)
icons.append(enter_room)

exit_room = game.sprite.Sprite()
exit_room.image = game.image.load('Img/Dungeon/exit.png')
exit_room.rect = Rect(1580, 805, 50, 50)
icons.append(exit_room)

attack_soon = game.sprite.Sprite()
attack_soon.image = game.image.load('Img/Dungeon/attack_soon.png')
attack_soon.rect = Rect(1580, 805, 50, 50)

attack_never = game.sprite.Sprite()
attack_never.image = game.image.load('Img/Dungeon/attack_never.png')
attack_never.rect = Rect(1580, 805, 50, 50)
########################################################################################################################

# Основные переменные цикла
running = True
in_battle = False
counter = 30
enemy_counter = 10

# Главный цикл
while running:
    game.time.Clock().tick(int(config['FPS']))
    screen.fill(BLACK)
    events = game.event.get()

    if layout == 'main_menu':
        for button in menu_buttons:
            button.if_intersect(game.mouse.get_pos())

        for event in events:
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                for button in menu_buttons:
                    button.if_pressed(event)
    elif layout == 'dungeon':
        for event in events:
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    dodge('left')
                elif event.key == K_d:
                    dodge('right')
                elif event.key == K_w:
                    attack()
                elif event.key == K_LEFT:
                    move('left')
                elif event.key == K_RIGHT:
                    move('right')
                elif event.key == K_e:
                    interact()
                elif event.key == K_ESCAPE:
                    layout = 'main_menu'
                    game_status = 'normal'

    render()
    game.display.update()

    if in_battle:
        if counter > 0:
            counter -= 1
    else:
        counter = 30

    if in_battle:
        if enemy_counter > 0:
            enemy_counter -= 1
        else:
            # Атака по герою
            if enemy:
                if hero.rail == enemy.rail:
                    hero.hp -= enemy.dmg
                    if hero.hp <= 0:
                        if score > max_score:
                            change_max_score(score)
                        game_status = 'game_over'
                enemy.switch()
                enemy_counter = 10
