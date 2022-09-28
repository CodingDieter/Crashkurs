"""player class"""


class Player:
    counter = 0

    def __init__(self, name):
        self.name = name
        self.points = 0
        Player.counter += 1

    def addpoints(self, points):
        self.points += points

    def subpoints(self, points):
        if self.points <= 0:
            self.points == 0
        else:
            self.points -= points