#! /usr/bin/env python3

import argparse
import random

class MastermindPlayer(object):

  def __init__(self):
    pass

  def move(self):
    pass

  def update(self, outcome):
    pass

class MastermindHumanPlayer(MastermindPlayer):

  def __init__(self):
    pass

  def move(self):
    pass

  def update(self, outcome):
    pass

def random_secret():
  return [random.randint(1, 6) for _ in range(4)]

def format_row(row):
  return ', '.join(map(str, row))

class Mastermind(object):

  def __init__(self):
    self.print_header()
    self.secret = random_secret()
    self.finished = False
    self.turn_counter = 0
    self.turn_limit = 20

  def print_header(self):
    print("        MASTERMIND!!!!!")
    print("        X, X, X, X")

  def update_board(self, guess):
    print(format_row(self.grade_guess(guess)))

  def get_guess(self):
    return list(map(lambda x: int(x.strip()), input("Guess : ").split(',')))

  def print_win(self):
    print("Congratulations, you won!")

  def print_lose(self):
    print("Dude, you lost!")
    self.print_secret()

  def grade_guess(self, guess):
    cached_secret = self.secret[:]
    result = []
    for i, val in enumerate(cached_secret):
      if guess[i] == val:
        result.append("B")
        guess[i] = 0
        cached_secret[i] = -1
    for i, val in enumerate(cached_secret):
      if val in guess:
        result.append("W")
        guess[guess.index(val)] = 0
    random.shuffle(result)
    if result == ["B", "B", "B", "B"]:
      self.print_win()
      self.finished = True
    return result

  def play(self):
    #self.print_secret()
    if self.turn_counter > self.turn_limit:
      self.finished = True
      self.print_lose()
      return
    try:
      guess = self.get_guess()
    except ValueError:
      print("Bad guess, try again")
      self.play()
    self.update_board(guess)
    self.turn_counter += 1

  def print_secret(self):
    print("Secret: " + format_row(self.secret))

def play(game):
  while not game.finished:
    game.play()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  pad = parser.add_argument
  pad('--ai', default=False, action='store_true')
  args = parser.parse_args()
  mastermind = Mastermind()
  try:
    play(mastermind)
  except KeyboardInterrupt:
    print("")
    mastermind.print_secret()
