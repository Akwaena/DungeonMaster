import pygame as game
from pygame.locals import *
import Functions
from Tools.debugger import *
import DungeonGenerator

# Создание экрана, констант, цветов и тд
log('Dungeon/Начальная инициализация')

RESOLUTION = (1920, 1080)
FPS = 60

screen = game.display.set_mode(RESOLUTION)
game.display.set_caption('Мастер Подземелий')

save = Functions.Save()
save.load()

dungeon = DungeonGenerator.Dungeon(save.raids)
dungeon.ultra_simple_generator(10)
hero = Functions.Hero(dungeon.rooms[0], save)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (60, 100, 50)
BLUE = (0, 0, 255)
BROWN = (70, 50, 30)

game.font.init()
font_36 = game.font.Font('Data/Fonts/GothicRus.ttf', 36)
font_30 = game.font.Font('Data/Fonts/GothicRus.ttf', 30)
font_18 = game.font.Font('Data/Fonts/GothicRus.ttf', 18)

########################################
log('Dungeon/Начальная инициализация успешна')
########################################


# Функции
def render():
    if game_end:
        render_end()
        return
    for sprite in sprites_to_render:
        screen.blit(sprite.image, sprite.rect)

    screen.blit(font_36.render(f'{save.pocket_food} еды', True, BROWN), Rect(10, 800, 130, 60))
    screen.blit(font_36.render(f'{hero.hp} HP', True, DARK_GREEN), Rect(1215, 800, 100, 50))
    screen.blit(font_36.render(f'{hero.attack} DMG', True, DARK_GREEN), Rect(1215, 850, 100, 50))
    screen.blit(font_36.render(f'{hero.defence} DEF', True, DARK_GREEN), Rect(1215, 900, 100, 50))

    if in_battle:
        screen.blit(font_30.render('Призрачный', True, BLACK), Rect(1750, 800, 100, 50))
        screen.blit(font_30.render('казак', True, BLACK), Rect(1780, 830, 100, 50))
        screen.blit(font_36.render(f'{enemy.lvl} lvl', True, BLACK), Rect(1780, 880, 100, 50))
        screen.blit(font_36.render(f'{enemy.hp} HP', True, RED), Rect(1780, 930, 100, 50))

    if hero.current_rail == 0:
        hero_sprite.rect.x = 1420
        screen.blit(hero_sprite.image, hero_sprite.rect)
    elif hero.current_rail == 1:
        hero_sprite.rect.x = 1540
        screen.blit(hero_sprite.image, hero_sprite.rect)
    elif hero.current_rail == 2:
        hero_sprite.rect.x = 1670
        screen.blit(hero_sprite.image, hero_sprite.rect)

    if enemy:
        if enemy.attack_rail == 0:
            attack_soon.rect.x = 1460
            screen.blit(attack_soon.image, attack_soon.rect)
        else:
            attack_never.rect.x = 1460
            screen.blit(attack_never.image, attack_never.rect)
        if enemy.attack_rail == 1:
            attack_soon.rect.x = 1580
            screen.blit(attack_soon.image, attack_soon.rect)
        else:
            attack_never.rect.x = 1580
            screen.blit(attack_never.image, attack_never.rect)
        if enemy.attack_rail == 2:
            attack_soon.rect.x = 1700
            screen.blit(attack_soon.image, attack_soon.rect)
        else:
            attack_never.rect.x = 1700
            screen.blit(attack_never.image, attack_never.rect)

    mod = 100
    dungeon.render(screen, icons, 50, 50, mod)
    hero_room.rect.x = (hero.room.id + 1) * mod + 50
    screen.blit(hero_room.image, hero_room.rect)


def render_end():
    global game_end
    if game_end == 'good':
        screen.blit(good_end.image, good_end.rect)
    if game_end == 'neutral':
        screen.blit(neutral_end.image, neutral_end.rect)
    if game_end == 'dead':
        print('Произошла смэрть')
        screen.blit(death_end.image, death_end.rect)


def move(direction):
    if not in_battle:
        if direction == 'east':
            if len(dungeon.rooms) > hero.room.id + 1:
                hero.room = dungeon.rooms[hero.room.id + 1]
                log(f'Dungeon/Совершено движение на {direction}')
        elif direction == 'west':
            if hero.room.id > 0:
                hero.room = dungeon.rooms[hero.room.id - 1]
                log(f'Dungeon/Совершено движение на {direction}')


def dodge(direction):
    if in_battle:
        log(f'Dungeon/Совершен уворот в {direction}')
        if direction == 'left':
            if hero.current_rail > 0:
                hero.current_rail -= 1
        if direction == 'right':
            if hero.current_rail < 2:
                hero.current_rail += 1


def attack():
    global in_battle
    global strike_cooldown
    global standard_cooldowns
    if in_battle:
        log('Dungeon/Совершена атака')
    else:
        return
    if enemy:
        if strike_cooldown <= 0:
            enemy.hp -= hero.attack
            strike_cooldown = standard_cooldowns[0]
            if enemy.hp <= 0:
                in_battle = False
                hero.room.inside = 'loot'


def interact():
    global in_battle
    global enemy
    global strike_cooldown
    global dodge_window
    global standard_cooldowns
    global game_end
    log('Dungeon/Производится интеракция с комнатой')
    if hero.room.inside == 'loot':
        save.pocket_food += 3
        hero.room.inside = 'empty'

    if hero.room.inside == 'enemy':
        if not in_battle:
            enemy = Functions.Monster(save.raids)
            in_battle = True
            strike_cooldown = hero.fight_speed
            dodge_window = hero.dodge_window
            standard_cooldowns = (strike_cooldown, dodge_window)

    if hero.room.inside == 'exit':
        game_end = 'neutral'
    elif hero.room.inside == 'enter':
        game_end = 'good'


#########


# Загрузка спрайтов
log('Dungeon/Загрузка спрайтов')

sprites_to_render = []
icons = []

background = game.sprite.Sprite()
background.image = game.image.load('Data/Img/Dungeon/Background.png')
background.rect = Rect(0, 0, 1920, 1080)
sprites_to_render.append(background)

good_end = game.sprite.Sprite()
good_end.image = game.image.load('Data/Img/Backgrounds/good_end.png')
good_end.rect = Rect(0, 0, 1920, 1080)

neutral_end = game.sprite.Sprite()
neutral_end.image = game.image.load('Data/Img/Backgrounds/neutral_end.png')
neutral_end.rect = Rect(0, 0, 1920, 1080)

death_end = game.sprite.Sprite()
death_end.image = game.image.load('Data/Img/Backgrounds/dead_end.png')
death_end.rect = Rect(0, 0, 1920, 1080)

hero_sprite = game.sprite.Sprite()
hero_sprite.image = game.image.load('Data/Img/Dungeon/hero.png')
hero_sprite.rect = Rect(1540, 1020, 100, 50)

attack_soon = game.sprite.Sprite()
attack_soon.image = game.image.load('Data/Img/Dungeon/attack_soon.png')
attack_soon.rect = Rect(1580, 805, 50, 50)

attack_never = game.sprite.Sprite()
attack_never.image = game.image.load('Data/Img/Dungeon/attack_never.png')
attack_never.rect = Rect(1580, 805, 50, 50)

empty_room = game.sprite.Sprite()
empty_room.image = game.image.load('Data/Img/Dungeon/empty.png')
empty_room.rect = Rect(1580, 805, 50, 50)
icons.append(empty_room)

enemy_room = game.sprite.Sprite()
enemy_room.image = game.image.load('Data/Img/Dungeon/enemy.png')
enemy_room.rect = Rect(1580, 805, 50, 50)
icons.append(enemy_room)

loot_room = game.sprite.Sprite()
loot_room.image = game.image.load('Data/Img/Dungeon/loot.png')
loot_room.rect = Rect(1580, 805, 50, 50)
icons.append(loot_room)

enter_room = game.sprite.Sprite()
enter_room.image = game.image.load('Data/Img/Dungeon/enter.png')
enter_room.rect = Rect(1580, 805, 50, 50)
icons.append(enter_room)

exit_room = game.sprite.Sprite()
exit_room.image = game.image.load('Data/Img/Dungeon/exit.png')
exit_room.rect = Rect(1580, 805, 50, 50)
icons.append(exit_room)

hero_room = game.sprite.Sprite()
hero_room.image = game.image.load('Data/Img/Dungeon/hero_room.png')
hero_room.rect = Rect(1580, 550, 50, 50)

###################
log('Dungeon/Спрайты загружены')
###################

# Главный цикл
log('Dungeon/Вход в главный цикл')

running = True
next_page = None
in_battle = False
enemy = None
game_end = False
strike_cooldown = 0
dodge_window = 0
standard_cooldowns = ()

while running:
    game.time.Clock().tick(FPS)
    screen.fill(BLACK)
    events = game.event.get()

    for event in events:
        if event.type == QUIT:
            running = False
            log('Dungeon/Выход из главного цикла')
        elif event.type == event.type == KEYDOWN:
            if event.key == K_SPACE:
                log('Dungeon/Нажат пробел')
                attack()
            elif event.key == K_a:
                log('Dungeon/Нажата А')
                dodge('left')
            elif event.key == K_d:
                log('Dungeon/Нажата D')
                dodge('right')
            elif event.key == K_UP:
                log('Dungeon/Нажата стрелка вверх')
                move('north')
            elif event.key == K_DOWN:
                log('Dungeon/Нажата стрелка вниз')
                move('south')
            elif event.key == K_LEFT:
                log('Dungeon/Нажата стрелка влево')
                move('west')
            elif event.key == K_RIGHT:
                log('Dungeon/Нажата стрелка вправо')
                move('east')
            elif event.key == K_e:
                log('Dungeon/Нажата Е')
                interact()
            elif event.key == K_t:
                log('Dungeon/Нажат Ctrl')
                enemy.attack()
            elif event.key == K_ESCAPE:
                log('Dungeon/Нажат ESC')
                if game_end == 'dead':
                    save.clear()
                    exit()
                elif game_end == 'neutral':
                    save.clear()
                    exit()
                elif game_end == 'good':
                    running = False
    if in_battle:
        if strike_cooldown >= 1:
            strike_cooldown -= 1
        if dodge_window >= 1:
            dodge_window -= 10
        else:
            if hero.current_rail == enemy.attack_rail:
                dodge_window = standard_cooldowns[1]
                hero.hp -= 10
                if hero.hp <= 0:
                    game_end = 'dead'
                    in_battle = False
                enemy.attack()
            else:
                dodge_window = standard_cooldowns[1]
                enemy.attack()

    render()
    game.display.update()

if game_end == 'good':
    save.xp += 1
    save.raids += 1
    save.save()
    import RaidPreparation
