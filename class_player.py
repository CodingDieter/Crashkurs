"""player class"""


class Player:
  def __init__(self, name):
    self.name = name
    self.points = 0

  def addpoints(self, points):
    self.points += points

  def subpoints(self, points):
    self.points -= points
    if self.points < 0:
      self.points == 0


