from pygame.locals import *


class Button:
    """Кнопка"""
    def __init__(self, sprite, pressed_state, function=None):
        # pressed_state = только image
        self.rect = sprite.rect
        self.image = sprite.image
        self.idle = sprite.image
        self.pressed = pressed_state
        if function:
            self.function = function

    def connect(self, function):
        """Подключить функцию к кнопке"""
        self.function = function

    def if_intersect(self, dot):
        """Проверка пересечения курсора и кнопки"""
        if self.rect.collidepoint(dot):
            self.image = self.pressed
            return True
        else:
            self.image = self.idle

    def if_pressed(self, event):
        """Проверка нажатия на кнопку"""
        if event.type == MOUSEBUTTONDOWN:
            if self.if_intersect(event.pos):
                self.function()
                return True
        return False

    def render(self, screen):
        """Отрисовка кнопки"""
        screen.blit(self.image, self.rect)
