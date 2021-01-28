import pygame as game
from pygame.locals import *
import Functions
from Tools.debugger import *
from Data.Items.Weapons import *
from Data.Items.Armor import *
from Data.Items.Artifacts import *

# Создание экрана
RESOLUTION = (1920, 1080)
FPS = 60
screen = game.display.set_mode(RESOLUTION)
game.display.set_caption('Мастер Подземелий')

screen_buttons = []
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (70, 50, 30)
RED = (255, 0, 0)

save = Functions.Save()
save.load()
#################
log('IntroCutscene/Создан экран')
#################

# Подгрузка шрифтов
game.font.init()
font_36 = game.font.Font('Data/Fonts/GothicRus.ttf', 36)
###################
log(f'RaidPreparations/Подгружены шрифты {game.font.get_fonts()}')


###################

# Функции кнопок
def weapon_left():
    if save.all_weapon[save.weapon] == 't':
        if save.weapon > 0:
            save.weapon -= 1
            return
        else:
            save.weapon = 6
    while save.all_weapon[save.weapon] == 'f':
        if save.weapon > 0:
            save.weapon -= 1
        else:
            save.weapon = 6

    log('RaidPreparations/Выбор оружия прокручен влево')


def weapon_right():
    if save.all_weapon[save.weapon] == 't':
        if save.weapon < 6:
            save.weapon += 1
        else:
            save.weapon = 0
        return
    while save.all_weapon[save.weapon] == 'f':
        if save.weapon < 6:
            save.weapon += 1
        else:
            save.weapon = 0

    log('RaidPreparations/Выбор оружия прокручен вправо')


def armor_left():
    if save.all_armor[save.armor] == 't':
        if save.armor > 0:
            save.armor -= 1
            return
        else:
            save.armor = 3
    while save.all_armor[save.armor] == 'f':
        if save.armor > 0:
            save.armor -= 1
        else:
            save.armor = 3

    log('RaidPreparations/Выбор брони прокручен влево')


def armor_right():
    if save.all_armor[save.armor] == 't':
        if save.armor < 3:
            save.armor += 1
        else:
            save.armor = 0
        return
    while save.all_weapon[save.armor] == 'f':
        if save.armor < 3:
            save.armor += 1
        else:
            save.armor = 0

    log('RaidPreparations/Выбор брони прокручен вправо')


def artifact_left():
    if save.all_artifact[save.artifact] == 't':
        if save.artifact > 0:
            save.artifact -= 1
            return
        else:
            save.artifact = 2
    while save.all_artifact[save.artifact] == 'f':
        if save.artifact > 0:
            save.artifact -= 1
        else:
            save.artifact = 2

    log('RaidPreparations/Выбор брони прокручен влево')


def artifact_right():
    if save.all_artifact[save.artifact] == 't':
        if save.artifact < 2:
            save.artifact += 1
        else:
            save.artifact = 0
        return
    while save.all_artifact[save.artifact] == 'f':
        if save.artifact < 2:
            save.artifact += 1
        else:
            save.artifact = 0

    log('RaidPreparations/Выбор брони прокручен вправо')


def pick_food():
    if save.stock_food > 2:
        save.stock_food -= 3
        save.pocket_food += 3

    log('RaidPreparations/Взята еда со склада')


def leave_food():
    if save.pocket_food > 2:
        save.stock_food += 3
        save.pocket_food -= 3

    log('RaidPreparations/Еда положена на склад')


def start():
    global running
    global next_page
    running = False
    next_page = 'Dungeon'


def skill_page():
    global running
    global next_page
    # running = False
    next_page = 'Skills'


def render():
    screen.blit(weapon_back_sprite.image, weapon_back_sprite.rect)
    screen.blit(font_36.render('Оружие', True, WHITE), Rect(1445, 50, 100, 45))
    screen.blit(font_36.render(weapons[save.weapon].name, True, WHITE), Rect(1350, 130, 500, 45))
    screen.blit(font_36.render(f'{weapons[save.weapon].dmg} урона', True, WHITE), Rect(1350, 180, 500, 45))

    screen.blit(armor_back_sprite.image, armor_back_sprite.rect)
    screen.blit(font_36.render('Броня', True, WHITE), Rect(1445, 380, 100, 45))
    screen.blit(font_36.render(armor[save.armor].name, True, WHITE), Rect(1350, 470, 1000, 45))
    screen.blit(font_36.render(f'Покрытие {armor[save.armor].cover}%', True, WHITE), Rect(1350, 510, 500, 45))
    screen.blit(font_36.render(f'Защита {armor[save.armor].defence}', True, WHITE), Rect(1350, 560, 500, 45))

    screen.blit(artifact_back_sprite.image, artifact_back_sprite.rect)
    screen.blit(font_36.render('Артефакт', True, WHITE), Rect(1445, 750, 100, 45))
    screen.blit(font_36.render(artifacts[save.artifact].name, True, WHITE), Rect(1350, 830, 1000, 45))
    screen.blit(font_36.render(f'{artifacts[save.artifact].buff}', True, WHITE), Rect(1350, 890, 500, 45))

    screen.blit(font_36.render(f'{save.stock_food} еды в кладовке', True, BROWN), Rect(30, 30, 100, 45))
    screen.blit(font_36.render(f'-{save.all_consumption} еды/день', True, RED), Rect(400, 30, 100, 45))
    screen.blit(font_36.render(f'{save.pocket_food} еды с собой', True, BROWN), Rect(30, 70, 100, 45))
    screen.blit(font_36.render(f'-3 еды/день', True, RED), Rect(400, 70, 100, 45))

    screen.blit(font_36.render(f'Члены семьи:', True, WHITE), Rect(30, 380, 100, 45))
    screen.blit(font_36.render(f'Надежда: {save.hope}', True, WHITE), Rect(850, 380, 100, 45))

    for button in screen_buttons:
        button.render(screen)

    screen.blit(font_36.render(f'{save.xp} xp', True, BLACK), Rect(1350, 1005, 100, 45))
    counter = 1
    for i in save.family:
        i.render(screen, font_36, 450 + (70 * counter))
        counter += 1


################
log('RaidPreparations/Заданы функции')
################

# Подгрузка спрайтов
weapon_left_button = game.image.load('Data/Img/Buttons/PreTypeLeft.png')
weapon_left_button_sprite = game.sprite.Sprite()
weapon_left_button_sprite.image = weapon_left_button
weapon_left_button_sprite.rect = weapon_left_button_sprite.image.get_rect()
weapon_left_button_sprite.rect.x = 1740
weapon_left_button_sprite.rect.y = 100
screen_buttons.append(Functions.Button(weapon_left_button_sprite, 'w_left', weapon_left))

weapon_right_button = game.image.load('Data/Img/Buttons/PreTypeRight.png')
weapon_right_button_sprite = game.sprite.Sprite()
weapon_right_button_sprite.image = weapon_right_button
weapon_right_button_sprite.rect = weapon_right_button_sprite.image.get_rect()
weapon_right_button_sprite.rect.x = 1090
weapon_right_button_sprite.rect.y = 100
screen_buttons.append(Functions.Button(weapon_right_button_sprite, 'w_right', weapon_right))

weapon_back = game.image.load('Data/Img/Buttons/PreTypeButton.png')
weapon_back_sprite = game.sprite.Sprite()
weapon_back_sprite.image = weapon_back
weapon_back_sprite.rect = weapon_back_sprite.image.get_rect()
weapon_back_sprite.rect.x = 1240
weapon_back_sprite.rect.y = 100

armor_left_button = game.image.load('Data/Img/Buttons/PreTypeLeft.png')
armor_left_button_sprite = game.sprite.Sprite()
armor_left_button_sprite.image = armor_left_button
armor_left_button_sprite.rect = armor_left_button_sprite.image.get_rect()
armor_left_button_sprite.rect.x = 1740
armor_left_button_sprite.rect.y = 450
screen_buttons.append(Functions.Button(armor_left_button_sprite, 'a_left', armor_left))

armor_right_button = game.image.load('Data/Img/Buttons/PreTypeRight.png')
armor_right_button_sprite = game.sprite.Sprite()
armor_right_button_sprite.image = armor_right_button
armor_right_button_sprite.rect = armor_right_button_sprite.image.get_rect()
armor_right_button_sprite.rect.x = 1090
armor_right_button_sprite.rect.y = 450
screen_buttons.append(Functions.Button(armor_right_button_sprite, 'a_right', armor_right))

armor_back = game.image.load('Data/Img/Buttons/PreTypeButton.png')
armor_back_sprite = game.sprite.Sprite()
armor_back_sprite.image = armor_back
armor_back_sprite.rect = armor_back_sprite.image.get_rect()
armor_back_sprite.rect.x = 1240
armor_back_sprite.rect.y = 450

artifact_left_button = game.image.load('Data/Img/Buttons/PreTypeLeft.png')
artifact_left_button_sprite = game.sprite.Sprite()
artifact_left_button_sprite.image = artifact_left_button
artifact_left_button_sprite.rect = artifact_left_button_sprite.image.get_rect()
artifact_left_button_sprite.rect.x = 1740
artifact_left_button_sprite.rect.y = 800
screen_buttons.append(Functions.Button(artifact_left_button_sprite, 'art_left', artifact_left))

artifact_right_button = game.image.load('Data/Img/Buttons/PreTypeRight.png')
artifact_right_button_sprite = game.sprite.Sprite()
artifact_right_button_sprite.image = artifact_right_button
artifact_right_button_sprite.rect = artifact_right_button_sprite.image.get_rect()
artifact_right_button_sprite.rect.x = 1090
artifact_right_button_sprite.rect.y = 800
screen_buttons.append(Functions.Button(artifact_right_button_sprite, 'art_right', artifact_right))

artifact_back = game.image.load('Data/Img/Buttons/PreTypeButton.png')
artifact_back_sprite = game.sprite.Sprite()
artifact_back_sprite.image = artifact_back
artifact_back_sprite.rect = artifact_back_sprite.image.get_rect()
artifact_back_sprite.rect.x = 1240
artifact_back_sprite.rect.y = 800

pick_food_button = game.image.load('Data/Img/Buttons/pick_3food.png')
pick_food_button_sprite = game.sprite.Sprite()
pick_food_button_sprite.image = pick_food_button
pick_food_button_sprite.rect = pick_food_button_sprite.image.get_rect()
pick_food_button_sprite.rect.x = 30
pick_food_button_sprite.rect.y = 160
screen_buttons.append(Functions.Button(pick_food_button_sprite, 'pick', pick_food))

leave_food_button = game.image.load('Data/Img/Buttons/leave_3food.png')
leave_food_button_sprite = game.sprite.Sprite()
leave_food_button_sprite.image = leave_food_button
leave_food_button_sprite.rect = leave_food_button_sprite.image.get_rect()
leave_food_button_sprite.rect.x = 250
leave_food_button_sprite.rect.y = 160
screen_buttons.append(Functions.Button(leave_food_button_sprite, 'leave', leave_food))

enter_dungeon_button = game.image.load('Data/Img/Buttons/enter_dungeon.png')
enter_dungeon_button_sprite = game.sprite.Sprite()
enter_dungeon_button_sprite.image = enter_dungeon_button
enter_dungeon_button_sprite.rect = enter_dungeon_button_sprite.image.get_rect()
enter_dungeon_button_sprite.rect.x = 1500
enter_dungeon_button_sprite.rect.y = 1000
screen_buttons.append(Functions.Button(enter_dungeon_button_sprite, 'enter', start))

enter_skills_page_button = game.image.load('Data/Img/Buttons/skills_menu_enter.png')
enter_skills_page_button_sprite = game.sprite.Sprite()
enter_skills_page_button_sprite.image = enter_skills_page_button
enter_skills_page_button_sprite.rect = enter_skills_page_button_sprite.image.get_rect()
enter_skills_page_button_sprite.rect.x = 1050
enter_skills_page_button_sprite.rect.y = 1000
screen_buttons.append(Functions.Button(enter_skills_page_button_sprite, 'skills', skill_page))
####################
log('RaidPreparations/Подгружены спрайты')
####################

log('RaidPreparation/Успешная инициализация')
log('RaidPreparation/Вход в главный цикл')

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

    if next_page == 'Skills':
        print(123)
        print(next_page)
        import SkillPage
        next_page = None

##############
log('RaidPreparation/Покинут главный цикл')
save.save()
log('RaidPreparation/Конец программы')

if next_page == 'Dungeon':
    import Dungeon
    exit(0)
