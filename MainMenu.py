import pygame as game
from pygame.locals import *

import Functions
from Tools.debugger import *

# Создание экрана
RESOLUTION = (1920, 1080)
FPS = 60
screen = game.display.set_mode(RESOLUTION)
game.display.set_caption('Мастер Подземелий')
#################
log('MainMenu/Создан экран')
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
big_logo_sprite.rect.x = 1220
big_logo_sprite.rect.y = 0
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
new_game_button_sprite.rect.x = 1250
new_game_button_sprite.rect.y = 350

load_button = game.image.load('Data/Img/Buttons/load_button.png')
load_button_sprite = game.sprite.Sprite()
load_button_sprite.image = load_button
load_button_sprite.rect = load_button_sprite.image.get_rect()
load_button_sprite.rect.x = 1250
load_button_sprite.rect.y = 510

settings_button = game.image.load('Data/Img/Buttons/settings_button.png')
settings_button_sprite = game.sprite.Sprite()
settings_button_sprite.image = settings_button
settings_button_sprite.rect = settings_button_sprite.image.get_rect()
settings_button_sprite.rect.x = 1250
settings_button_sprite.rect.y = 670

exit_button = game.image.load('Data/Img/Buttons/exit_button.png')
exit_button_sprite = game.sprite.Sprite()
exit_button_sprite.image = exit_button
exit_button_sprite.rect = exit_button_sprite.image.get_rect()
exit_button_sprite.rect.x = 1250
exit_button_sprite.rect.y = 900
####################
# Процесс можно пользователю загрузкой показывать
log('MainMenu/Подгружены спрайты')


####################


# Функции кнопок
def open_settings():
    """Переход в настройки"""
    log('MainMenu/Нажата кнопка настройки')
    pass


def open_load_screen():
    """Переход в меню загрузки игры"""
    log('MainMenu/Нажата кнопка загрузить')
    pass


def open_new_game_screen():
    """Переход к началу новой игры"""
    global running
    global next_page
    log('MainMenu/Нажата кнопка новая игра')
    running = False
    next_page = 'IntroCutscene'

    Functions.Save().clear()


def exit_event():
    """Штатный выход из игры"""
    global running
    log('MainMenu/Нажата кнопка выхода')
    running = False


################
log('MainMenu/Заданы функции')


################

# Функция рендера
# Возможно, лучше универсализировать

def render():
    screen.blit(menu_background_sprite.image, menu_background_sprite.rect)
    game.draw.rect(screen, BLACK, (1220, 0, 700, 1080))
    for i in screen_buttons:
        i.render(screen)


# Всякие константы
downed_buttons = []
down_dot = None
mouse_buttons = ('LMouse', 'MMouse', 'RMouse')
screen_buttons = (Functions.Button(exit_button_sprite, 'exit', exit_event),
                  Functions.Button(settings_button_sprite, 'settings', open_settings),
                  Functions.Button(load_button_sprite, 'load', open_load_screen),
                  Functions.Button(new_game_button_sprite, 'new game', open_new_game_screen))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
##################
log('MainMenu/Заданы константы')
##################

log('MainMenu/Успешная инициализация')
log('MainMenu/Вход в главный цикл')

# Главный цикл
running = True
next_page = None
while running:
    game.time.Clock().tick(FPS)
    screen.fill(BLACK)
    events = game.event.get()

    for event in events:
        if event.type == QUIT:
            # УДАЛИТЬ
            running = False
            log('MainMenu/Главный цикл: выход из цикла')
        if event.type == MOUSEBUTTONDOWN:
            log(f'MainMenu/Главный цикл: нажатие кнопки мыши в точке {event.pos}')
            down_dot = Functions.Dot(event.pos)
        if event.type == MOUSEBUTTONUP:
            log(f'MainMenu/Главный цикл: отжатие кнопки мыши в точке {event.pos}')
            if down_dot:
                down_button = Functions.collide_button(screen_buttons, down_dot)
                if down_button == Functions.collide_button(screen_buttons, Functions.Dot(event.pos)):
                    if down_button:
                        down_button.function()

    render()
    game.display.update()

##############
log('MainMenu/Покинут главный цикл')
# Сюда можно еще чего-нибудь закинуть
log('MainMenu/Конец программы')

if next_page == 'IntroCutscene':
    import IntroCutscene
    exit(0)
elif next_page == 'SettingsPage':
    exit(0)
