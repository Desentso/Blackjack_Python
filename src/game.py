import random

from Card import Card
from Player import Player

NUMBER_OF_DECKS = 4
PLAYER_START_MONEY = 100

class Game:
  def __init__(self):
    self.cards = []
    self.player = Player(PLAYER_START_MONEY)

    self.dealer_cards = []

    self.generate_cards()


  def generate_cards(self):
    cards = []
    for deck in range(NUMBER_OF_DECKS):
      for region in range(4):
        for value in range(2, 14):
          cards.append(Card(region, value))

    self.cards = cards


  def check_blackjack(self):
    summ = 0
    for card in self.player.cards:
      summ += card.value

    return summ == 21


  def draw_card(self):
    card_index = random.randrange(0, len(self.cards))
    card = self.cards[card_index]
    del self.cards[card_index]
    return card


  def player_won(self):
    print("You won!")

  def start_game(self):

    print("Hello, welcome to play Blackjack!")

    while True:
      self.player.ask_for_bet()

      self.player.add_card(self.draw_card())
      self.player.add_card(self.draw_card())

      self.player.print_cards()

      if self.check_blackjack():
        self.player_won()
        continue

      break


if __name__ == "__main__":
  game = Game()
  game.start_game()
  pass
