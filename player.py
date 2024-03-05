import math
import random

class Player:
  def __init__(self, latter):
    self.letter = latter
  def get_move(self, game):
    pass

class RandomComputerPlayer(Player):
  def __init__ (self, letter):
    super().__init__(letter)
  def get_move(self, game):
    square = random.choice(game.available_moves())
    return square

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  def get_move(self, game):
    valid_square = False
    val = None
    while not valid_square:
      square = input(self.letter + "\"s 당신차례입니다. 위치를 선택해 주세요. (0-8): ")
      try:
        val = int(square)
        if val not in game.available_moves():
          raise ValueError
        valid_square = True
      except ValueError:
        print("선택할 수 없는 값입니다. 다시 시도해주세요.")