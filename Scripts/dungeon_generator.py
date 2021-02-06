from random import shuffle


class Dungeon:
    """Подземелье"""
    def __init__(self):
        self.rooms = []

    def __getitem__(self, item):
        return self.rooms[item]

    def generate(self, room_num=7):
        """
        Генерация подземелья
        """
        self.rooms.clear()
        self.rooms.append(Room(0, 'enter'))
        insides = ['loot', 'enemy', 'empty', 'loot', 'enemy', 'empty', 'loot', 'enemy', 'empty', 'enemy']
        for i in range(room_num):
            shuffle(insides)
            self.rooms.append(Room(i + 1, insides[0]))
        self.rooms.append(Room(room_num + 1, 'exit'))

    def render(self, screen, icons, left=10, top=10, mod=10):
        """
        Отрисовка подземелья
        """
        for i in self.rooms:
            if i.inside == 'enemy':
                icon = icons[1]
                icon.rect.x = left + ((i.id + 1) * mod)
                icon.rect.y = top + (5 * mod)
            elif i.inside == 'loot':
                icon = icons[2]
                icon.rect.x = left + ((i.id + 1) * mod)
                icon.rect.y = top + (5 * mod)
            elif i.inside == 'enter':
                icon = icons[3]
                icon.rect.x = left + ((i.id + 1) * mod)
                icon.rect.y = top + (5 * mod)
            elif i.inside == 'exit':
                icon = icons[4]
                icon.rect.x = left + ((i.id + 1) * mod)
                icon.rect.y = top + (5 * mod)
            elif i.inside == 'empty':
                icon = icons[0]
                icon.rect.x = left + ((i.id + 1) * mod)
                icon.rect.y = top + (5 * mod)
            else:
                return
            screen.blit(icon.image, icon.rect)


class Room:
    """Комната"""
    def __init__(self, r_id, inside):
        self.id = r_id
        self.inside = inside
