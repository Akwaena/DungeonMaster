from Functions import Buff


class Artifact:
    def __init__(self, name, buff, lvl, rare):
        self.name = name
        self.buff = buff
        self.lvl = lvl
        self.rare = rare

    def use_buff(self, target):
        pass


artifacts = (Artifact('Факел', Buff('точность', 10), 1, 0), Artifact('Старая книга', Buff('опыт', 10), 1, 10),
             Artifact('Зловонный брелок', Buff('спавн монстров', -5), 2, 5))
