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
log('IntroCutscene/Создан экран')
#################

# Создание основных переменных и констант
frames = []
current_frame = 0
counter = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#########################################
log('IntroCutscene/Созданы основные переменные и константы')
#########################################

# Подгрузка кадров катсцены
for i in range(10):
    image = game.image.load(f'Data/Img/Cutscene/Intro/frame_0{i + 1}.png')
    sprite = game.sprite.Sprite()
    sprite.image = image
    sprite.rect = sprite.image.get_rect()

    frames.append(sprite)
############################
log('IntroCutscene/Подгружены кадры катсцены')


############################


# Функция рендера
def render():
    global current_frame
    global counter

    screen.blit(frames[current_frame].image, frames[current_frame].rect)

    if counter == 600:
        log('IntroCutscene/Переход на следующий кадр катсцены')
        current_frame += 1
        counter = 0
    else:
        counter += 1


#################
log('IntroCutscene/Создана функция рендера')
#################

log('IntroCutscene/Успешная инициализация')
log('IntroCutscene/Вход в главный цикл')

# Основной цикл
running = True
while running:
    game.time.Clock().tick(FPS)
    screen.fill(BLACK)
    events = game.event.get()

    for event in events:
        if event.type == QUIT:
            # УДАЛИТЬ
            running = False
            log('IntroCutscene/Главный цикл: выход из цикла')
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                log('IntroCutscene/Нажат пробел')
                counter = 600
                log('IntroCutscene/Пропущен кадр катсцены')

    render()
    game.display.update()
    counter += 1

    if current_frame >= 10:
        # Заменить на переход дальше
        log('IntroCutscene/Катсцена окончена')
        running = False

log('IntroCutscene/Покинут главный цикл')
log('IntroCutscene/Конец программы')

import RaidPreparation
