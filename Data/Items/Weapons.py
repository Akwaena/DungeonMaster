from Functions import Buff


class Weapon:
    def __init__(self, dmg, name, rare, lvl=1, buff=None):
        self.dmg = dmg
        self.buff = buff
        self.name = name
        self.rare = rare
        self.lvl = lvl

    def hit(self, target):
        pass


weapons = (Weapon(0, 'Кулаки', 0), Weapon(2, 'Отцовский меч', 0), Weapon(1, 'Ржавый меч', 80),
           Weapon(3, 'Старый меч', 70), Weapon(3, 'Железный меч', 50), Weapon(4, 'Хороший железный меч', 40, 5),
           Weapon(6, 'Древний железный меч', 1, 5, 'buff'))
