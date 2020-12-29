import pygame as game
from pygame.locals import *


# Создание экрана
screen = game.display.set_mode((1920, 1080))
game.display.set_caption('Мастер Подземелий')
#################

# Подгрузка спрайтов
# Системные спрайты
cursor = game.image.load('Data/Img/Sys/cursor.png')
cur_sprite = game.sprite.Sprite()
cur_sprite.image = cursor
cur_sprite.rect = cur_sprite.image.get_rect()
# Логотипы
big_logo = game.image.load('Data/Img/Credits/big_logo.png')
big_logo_sprite = game.sprite.Sprite()
big_logo_sprite.image = big_logo
big_logo_sprite.rect = big_logo_sprite.image.get_rect()
# Оформление
# ПЕРЕДЕЛАТЬ
menu_background = game.image.load('Data/Img/Backgrounds/MainMenu/1.png')
menu_background_sprite = game.sprite.Sprite()
menu_background_sprite.image = menu_background
menu_background_sprite.rect = menu_background_sprite.image.get_rect()

empty_background = game.image.load('Data/img/Backgrounds/button_background.png')
empty_background_sprite = game.sprite.Sprite()
empty_background_sprite.image = empty_background
empty_background_sprite.rect = empty_background_sprite.image.get_rect()
# Кнопки
new_game_button = game.image.load('Data/Img/Buttons/new_game_button.png')
new_game_button_sprite = game.sprite.Sprite()
new_game_button_sprite.image = new_game_button
new_game_button_sprite.rect = new_game_button_sprite.image.get_rect()

load_button = game.image.load('Data/Img/Buttons/load_button.png')
load_button_sprite = game.sprite.Sprite()
load_button_sprite.image = load_button
load_button_sprite.rect = load_button_sprite.image.get_rect()

settings_button = game.image.load('Data/Img/Buttons/settings_button.png')
settings_button_sprite = game.sprite.Sprite()
settings_button_sprite.image = settings_button
settings_button_sprite.rect = settings_button_sprite.image.get_rect()

exit_button = game.image.load('Data/Img/Buttons/exit_button.png')
exit_button_sprite = game.sprite.Sprite()
exit_button_sprite.image = exit_button
exit_button_sprite.rect = exit_button_sprite.image.get_rect()
####################

# Цвета
WHITE = (255, 255, 255)
BLACK = (255, 255, 255)
#######

downed_buttons = []
mouse_buttons = ('LMouse', 'MMouse', 'RMouse')


# Главный цикл
running = True
while running:
    game.time.Clock().tick(30)
    screen.fill(BLACK)
    events = game.event.get()

    for event in events:
        if event.type == QUIT:
            running = False
            exit()
        if event.type == MOUSEBUTTONDOWN:
            down_dot = Dot(event.pos)
        if event.type == MOUSEBUTTONUP:
            if 

##############
