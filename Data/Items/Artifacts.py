from Functions import Buff


class Artifact:
    def __init__(self, name, buff):
        self.name = name
        self.buff = buff

    def use_buff(self, target):
        pass


artifacts = (Artifact('Факел', Buff('точность', 10)), Artifact('Старая книга', Buff('опыт', 10)),
             Artifact('Зловонный брелок', Buff('спавн монстров', -5)))
