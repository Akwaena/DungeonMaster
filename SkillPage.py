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


# Установка функций
def render():
    for i in sprites_to_render:
        screen.blit(i.image, i.rect)

    for i in screen_buttons:
        i.render(screen)

    screen.blit(font_36.render(f'{save.xp} xp', True, WHITE), Rect(1500, 50, 100, 45))


def check_skills():
    convert_button('on', 'l_base', l_base)
    if save.skills[0] == 't':
        convert_button('learn', 'l_base', l_base)
        convert_button('on', 'l_att_1', l_att_1)
        convert_button('on', 'l_def_1', l_def_1)
        convert_button('on', 'l_dodge_1', l_dodge_1)
    if save.skills[1] == 't':
        convert_button('learn', 'l_att_1', l_att_1)
        convert_button('on', 'l_att_2', l_att_2)
    if save.skills[2] == 't':
        convert_button('learn', 'l_att_2', l_att_2)
        convert_button('g_block', 'l_invincible', l_invincible)
        convert_button('block', 'l_def_2', l_def_2)
    if save.skills[3] == 't':
        convert_button('learn', 'l_def_1', l_def_1)
        convert_button('on', 'l_def_2', l_def_2)
    if save.skills[4] == 't':
        convert_button('learn', 'l_def_2', l_def_2)
    if save.skills[5] == 't':
        convert_button('learn', 'l_dodge_1', l_dodge_1)
        convert_button('on', 'l_dodge_2', l_dodge_2)
    if save.skills[6] == 't':
        convert_button('learn', 'l_dodge_2', l_dodge_2)
        convert_button('g_block', 'l_invincible', l_invincible)
        convert_button('block', 'l_def_2', l_def_2)
    if save.skills[2] == 't' and save.skills[6] == 't':
        convert_button('g_on', 'l_ultrasonic', l_ultrasonic)
        convert_button('g_block', 'l_invincible', l_invincible)
    if save.skills[4] == 't' and save.skills[6] != 't' and save.skills[2] != 't':
        convert_button('g_on', 'l_invincible', l_invincible)
        convert_button('g_block', 'l_ultrasonic', l_ultrasonic)
    if save.skills[4] == 't':
        convert_button('g_block', 'l_ultrasonic', l_ultrasonic)
        convert_button('block', 'l_att_2', l_att_2)
        convert_button('block', 'l_dodge_2', l_dodge_2)
    if save.skills[7] == 't':
        convert_button('g_learn', 'l_ultrasonic', l_ultrasonic)
    if save.skills[8] == 't':
        convert_button('g_learn', 'l_invincible', l_invincible)


def convert_button(mode, button_name, origin_func):
    for i in screen_buttons:
        if i.name == button_name:
            if mode == 'on':
                i.image = game.image.load('Data/Img/Buttons/skill_available.png')
                i.function = origin_func
            elif mode == 'off':
                i.image = game.image.load('Data/Img/Buttons/skill_non_available.png')
                i.function = block
            elif mode == 'learn':
                i.image = game.image.load('Data/Img/Buttons/skill_learned.png')
                i.function = block
            elif mode == 'block':
                i.image = game.image.load('Data/Img/Buttons/skill_blocked.png')
                i.function = block
            elif mode == 'g_block':
                i.image = game.image.load('Data/Img/Buttons/great_skill_blocked.png')
                i.function = block
            elif mode == 'g_on':
                i.image = game.image.load('Data/Img/Buttons/great_skill_available.png')
                i.function = origin_func
            elif mode == 'g_off':
                i.image = game.image.load('Data/Img/Buttons/great_skill_non_available.png')
                i.function = block
            elif mode == 'g_learn':
                i.image = game.image.load('Data/Img/Buttons/great_skill_learned.png')
                i.function = block
            return


def learn(skill_id, cost=1):
    # split не работает почему-то
    if save.xp >= cost:
        skills = [i for i in save.skills]
        skills[skill_id] = 't'
        save.skills = ''.join(skills)
        check_skills()
        save.xp -= cost


def l_base():
    learn(0)
    log('SkillPage/Изучен базовый навык')
    log(f'SkillPage/Код навыков: {save.skills}')


def l_att_1():
    learn(1)
    log('SkillPage/Изучен 1 навык ветки атаки')
    log(f'SkillPage/Код навыков: {save.skills}')


def l_att_2():
    learn(2)
    log('SkillPage/Изучен 2 навык ветки атаки')
    log(f'SkillPage/Код навыков: {save.skills}')


def l_def_1():
    learn(3)
    log('SkillPage/Изучен 1 навык ветки защиты')
    log(f'SkillPage/Код навыков: {save.skills}')


def l_def_2():
    learn(4)
    log('SkillPage/Изучен 2 навык ветки защиты')
    log(f'SkillPage/Код навыков: {save.skills}')


def l_dodge_1():
    learn(5)
    log('SkillPage/Изучен 1 навык ветки уворота')
    log(f'SkillPage/Код навыков: {save.skills}')


def l_dodge_2():
    learn(6)
    log('SkillPage/Изучен 2 навык ветки уворота')
    log(f'SkillPage/Код навыков: {save.skills}')


def l_ultrasonic():
    learn(7)
    log('SkillPage/Изучен навык быстрого мастера')
    log(f'SkillPage/Код навыков: {save.skills}')


def l_invincible():
    learn(8)
    log('SkillPage/Изучен навык неуязвимого мастера')
    log(f'SkillPage/Код навыков: {save.skills}')


def block():
    log('SkillPage/Нажат заблокированый навык')


def back():
    global next_page
    global running
    next_page = 'RaidPreparation'
    running = False
    log('SkillPage/Возврат к подготовке к рейду')


###################
log('SkillPage/Функции установлены')
###################

# Загрузка спрайтов
screen_buttons = []
sprites_to_render = []

background = game.image.load('Data/Img/Backgrounds/SkillPage.png')
background_sprite = game.sprite.Sprite()
background_sprite.image = background
background_sprite.rect = background_sprite.image.get_rect()
sprites_to_render.append(background_sprite)

base_skill_button = game.image.load('Data/Img/Buttons/skill_non_available.png')
base_skill_button_sprite = game.sprite.Sprite()
base_skill_button_sprite.image = base_skill_button
base_skill_button_sprite.rect = base_skill_button_sprite.image.get_rect()
base_skill_button_sprite.rect.x = 1182
base_skill_button_sprite.rect.y = 658
screen_buttons.append(Functions.Button(base_skill_button_sprite, 'l_base', l_base))

att_1_skill_button = game.image.load('Data/Img/Buttons/skill_non_available.png')
att_1_skill_button_sprite = game.sprite.Sprite()
att_1_skill_button_sprite.image = att_1_skill_button
att_1_skill_button_sprite.rect = att_1_skill_button_sprite.image.get_rect()
att_1_skill_button_sprite.rect.x = 1282
att_1_skill_button_sprite.rect.y = 794
screen_buttons.append(Functions.Button(att_1_skill_button_sprite, 'l_att_1', l_att_1))

att_2_skill_button = game.image.load('Data/Img/Buttons/skill_non_available.png')
att_2_skill_button_sprite = game.sprite.Sprite()
att_2_skill_button_sprite.image = att_2_skill_button
att_2_skill_button_sprite.rect = att_2_skill_button_sprite.image.get_rect()
att_2_skill_button_sprite.rect.x = 1382
att_2_skill_button_sprite.rect.y = 937
screen_buttons.append(Functions.Button(att_2_skill_button_sprite, 'l_att_2', l_att_2))

dodge_1_skill_button = game.image.load('Data/Img/Buttons/skill_non_available.png')
dodge_1_skill_button_sprite = game.sprite.Sprite()
dodge_1_skill_button_sprite.image = dodge_1_skill_button
dodge_1_skill_button_sprite.rect = dodge_1_skill_button_sprite.image.get_rect()
dodge_1_skill_button_sprite.rect.x = 1282
dodge_1_skill_button_sprite.rect.y = 521
screen_buttons.append(Functions.Button(dodge_1_skill_button_sprite, 'l_dodge_1', l_dodge_1))

dodge_2_skill_button = game.image.load('Data/Img/Buttons/skill_non_available.png')
dodge_2_skill_button_sprite = game.sprite.Sprite()
dodge_2_skill_button_sprite.image = dodge_2_skill_button
dodge_2_skill_button_sprite.rect = dodge_2_skill_button_sprite.image.get_rect()
dodge_2_skill_button_sprite.rect.x = 1382
dodge_2_skill_button_sprite.rect.y = 383
screen_buttons.append(Functions.Button(dodge_2_skill_button_sprite, 'l_dodge_2', l_dodge_2))

def_1_skill_button = game.image.load('Data/Img/Buttons/skill_non_available.png')
def_1_skill_button_sprite = game.sprite.Sprite()
def_1_skill_button_sprite.image = def_1_skill_button
def_1_skill_button_sprite.rect = def_1_skill_button_sprite.image.get_rect()
def_1_skill_button_sprite.rect.x = 1082
def_1_skill_button_sprite.rect.y = 795
screen_buttons.append(Functions.Button(def_1_skill_button_sprite, 'l_def_1', l_def_1))

def_2_skill_button = game.image.load('Data/Img/Buttons/skill_non_available.png')
def_2_skill_button_sprite = game.sprite.Sprite()
def_2_skill_button_sprite.image = def_2_skill_button
def_2_skill_button_sprite.rect = def_2_skill_button_sprite.image.get_rect()
def_2_skill_button_sprite.rect.x = 982
def_2_skill_button_sprite.rect.y = 937
screen_buttons.append(Functions.Button(def_2_skill_button_sprite, 'l_def_2', l_def_2))

ultrasonic_skill_button = game.image.load('Data/Img/Buttons/great_skill_non_available.png')
ultrasonic_skill_button_sprite = game.sprite.Sprite()
ultrasonic_skill_button_sprite.image = ultrasonic_skill_button
ultrasonic_skill_button_sprite.rect = ultrasonic_skill_button_sprite.image.get_rect()
ultrasonic_skill_button_sprite.rect.x = 510
ultrasonic_skill_button_sprite.rect.y = 107
screen_buttons.append(Functions.Button(ultrasonic_skill_button_sprite, 'l_ultrasonic', l_ultrasonic))

invincible_skill_button = game.image.load('Data/Img/Buttons/great_skill_non_available.png')
invincible_skill_button_sprite = game.sprite.Sprite()
invincible_skill_button_sprite.image = invincible_skill_button
invincible_skill_button_sprite.rect = invincible_skill_button_sprite.image.get_rect()
invincible_skill_button_sprite.rect.x = 110
invincible_skill_button_sprite.rect.y = 107
screen_buttons.append(Functions.Button(invincible_skill_button_sprite, 'l_invincible', l_invincible))

back_button = game.image.load('Data/Img/Buttons/Back.png')
back_button_sprite = game.sprite.Sprite()
back_button_sprite.image = back_button
back_button_sprite.rect = back_button_sprite.image.get_rect()
back_button_sprite.rect.x = 50
back_button_sprite.rect.y = 1000
screen_buttons.append(Functions.Button(back_button_sprite, 'back_button', back))

check_skills()
###################
log('SkillPage/Спрайты установлены')
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
            log('SkillPage/Главный цикл: выход из цикла')
        if event.type == MOUSEBUTTONDOWN:
            log(f'SkillPage/Главный цикл: нажатие кнопки мыши в точке {event.pos}')
            down_dot = Functions.Dot(event.pos)
        if event.type == MOUSEBUTTONUP:
            log(f'SkillPage/Главный цикл: отжатие кнопки мыши в точке {event.pos}')
            if down_dot:
                down_button = Functions.collide_button(screen_buttons, down_dot)
                if down_button == Functions.collide_button(screen_buttons, Functions.Dot(event.pos)):
                    if down_button:
                        down_button.function()

    render()
    game.display.update()


if next_page == 'RaidPreparation':
    del screen


