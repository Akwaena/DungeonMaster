import pygame as game
from pygame.locals import *

import Functions
from Tools.debugger import *

# Создание экрана
RESOLUTION = (1920, 1080)
FPS = 60
screen = game.display.set_mode(RESOLUTION)
game.display.set_caption('Мастер Подземелий')

save = Functions.Save()
save.load()
#################
log('SkillPage/Создан экран')
#################

# Установка цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (70, 50, 30)
###################
log('SkillPage/Цвета установлены')
###################

# Подгрузка шрифтов
game.font.init()
font_36 = game.font.Font('Data/Fonts/GothicRus.ttf', 36)
###################
log(f'SkillPage/Подгружены шрифты {game.font.get_fonts()}')
###################

# Загрузка спрайтов
screen_buttons = []


###################
log('SkillPage/Спрайты установлены')
###################


# Установка функций
def render():
    for i in screen_buttons:
        i.render()


###################
log('SkillPage/Функции установлены')
###################

log('SkillPage/Успешная инициализация')
log('SkillPage/Вход в главный цикл')

# Главный цикл
running = True
next_page = None
down_dot = False
while running:
    game.time.Clock().tick(FPS)
    screen.fill(BLACK)
    events = game.event.get()

    for event in events:
        if event.type == QUIT:
            # УДАЛИТЬ
            running = False
            log('RaidPreparation/Главный цикл: выход из цикла')
        if event.type == MOUSEBUTTONDOWN:
            log(f'RaidPreparation/Главный цикл: нажатие кнопки мыши в точке {event.pos}')
            down_dot = Functions.Dot(event.pos)
        if event.type == MOUSEBUTTONUP:
            log(f'RaidPreparation/Главный цикл: отжатие кнопки мыши в точке {event.pos}')
            if down_dot:
                down_button = Functions.collide_button(screen_buttons, down_dot)
                if down_button == Functions.collide_button(screen_buttons, Functions.Dot(event.pos)):
                    if down_button:
                        down_button.function()

    render()
    game.display.update()
