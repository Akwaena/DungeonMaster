from Functions import Buff


class Armor:
    def __init__(self, name, covering_coeff, defence, rare, lvl=1, buff=None):
        self.name = name
        self.cover = covering_coeff
        self.defence = defence
        self.lvl = lvl
        self.buff = buff

    def absorb_hit(self, dmg, accuracy, player):
        pass


armor = (Armor('Старая кожанка', 70, 2, 0), Armor('Укрепленная кожанка', 20, 5, 60),
         Armor('Кожанка с латными вставками', 40, 7, 50), Armor('Ржавая кольчуга', 70, 6, 40))
