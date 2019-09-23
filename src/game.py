import random, time

from Card import Card
from Player import Player

NUMBER_OF_DECKS = 4
PLAYER_START_MONEY = 100

class Game:
  def __init__(self):
    self.cards = []
    self.player = Player(PLAYER_START_MONEY)

    self.dealer_cards = []
    self.dealer_total = 0

    self.generate_cards()


  def generate_cards(self):
    cards = []
    for deck in range(NUMBER_OF_DECKS):
      for region in range(4):
        for value in range(2, 15):
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


  def draw_card_for_dealer(self):
    card_drawn = self.draw_card()
    self.dealer_cards.append(card_drawn)
    self.dealer_total += card_drawn.value

    has_11 = False
    for card in self.dealer_cards:
      if card.value == 11:
        has_11 = card
        break

    if card_drawn.value == 11 and self.dealer_total > 21:
      card_drawn.value = 1
      self.dealer_total -= 10
    elif has_11 and self.dealer_total > 21:
      has_11.value = 1
      self.dealer_total -= 10

  def print_dealer_cards(self, show_2):
    print("Dealer's cards: ")
    if len(self.dealer_cards) == 2 and not show_2:
      print(self.dealer_cards[0], end=" ")
    else:
      for card in self.dealer_cards:
        print(card, end=" ")
      print("Total: {}".format(self.dealer_total), end=" ")

    print("\n")


  def player_won(self, is_blackjack = False):
    if is_blackjack:
      self.player.add_win(2.5)
    else:
      self.player.add_win(2)
    print("YOU WON!\n")


  def player_turn(self):
    print("Your turn!")

    command = 0

    while command != 2 and self.player.total < 21:
      self.player.print_cards()
      print("Would you like to")
      print("[1] Draw a card")
      print("[2] Stay")

      try:
        command = int(input())
      except Exception:
        command = 0
        pass

      if command == 1:
        self.player.add_card(self.draw_card())

    self.player.print_cards()
    if self.player.total > 21:
      print("You overdrew!")

    return

  #def dealer_cards_value(self):


  def dealer_turn(self):
    print("Dealer's turn!")
    self.print_dealer_cards(True)

    while self.dealer_total < 17:
      self.draw_card_for_dealer()
      self.print_dealer_cards(True)
      time.sleep(0.5)

  def check_win(self):
    if self.dealer_total > 21 and self.player.total <= 21:
      self.player_won(False)
    elif self.player.total <= 21 and self.player.total > self.dealer_total:
      self.player_won(False)
    elif self.player.total == self.dealer_total:
      print("IT'S A DRAW!\n")
      self.player.add_win(1)
    else:
      print("DEALER WON!\n")

  def reset_dealer(self):
    self.dealer_cards = []
    self.dealer_total = 0

  def end_of_round(self):
    self.player.reset()
    self.reset_dealer()

  def start_game(self):

    print("Hello, welcome to play Blackjack!")

    while self.player.money > 0:

      self.player.ask_for_bet()

      self.player.add_card(self.draw_card())
      self.player.add_card(self.draw_card())

      self.player.print_cards()

      if self.check_blackjack():
        self.player_won(True)
        self.end_of_round()
        continue

      self.draw_card_for_dealer()
      self.draw_card_for_dealer()

      self.print_dealer_cards(False)

      self.player_turn()
      print("--------------------\n")
      if self.player.total > 21:
        self.check_win()
        self.end_of_round()
        continue

      self.dealer_turn()

      print("--------------------\n")

      self.player.print_cards()
      self.print_dealer_cards(True)

      self.check_win()

      self.end_of_round()


if __name__ == "__main__":
  game = Game()
  game.start_game()
  pass
