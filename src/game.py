import random, time

from Card import Card, print_cards
from Player import Player

NUMBER_OF_DECKS = 4
PLAYER_START_MONEY = 100

class Game:
  def __init__(self):
    self.cards = []
    self.player = Player(PLAYER_START_MONEY, "player")
    self.dealer = Player(0, "dealer")

    self.generate_cards()


  def generate_cards(self):
    cards = []
    for deck in range(NUMBER_OF_DECKS):
      for region in range(4):
        for value in range(2, 15):
          cards.append(Card(region, value, value))

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


  def player_won(self, is_blackjack = False):
    if is_blackjack:
      self.player.add_win(2.5)
    else:
      self.player.add_win(2)
    print("YOU WON!\n")


  def player_turn(self):
    print("--------------------\n")
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


  def dealer_turn(self):
    print("--------------------\n")
    print("Dealer's turn!")
    self.dealer.print_cards(True)

    while self.dealer.total < 17:
      self.dealer.add_card(self.draw_card())
      self.dealer.print_cards(True)
      time.sleep(0.5)


  def check_win(self):
    if self.dealer.total > 21 and self.player.total <= 21:
      self.player_won(False)
    elif self.player.total <= 21 and self.player.total > self.dealer.total:
      self.player_won(False)
    elif self.player.total == self.dealer.total:
      print("IT'S A DRAW!\n")
      self.player.add_win(1)
    else:
      print("DEALER WON!\n")


  def end_of_round(self):
    self.player.reset()
    self.dealer.reset()


  def start_of_round(self):
    self.player.ask_for_bet()

    self.player.add_card(self.draw_card())
    self.player.add_card(self.draw_card())

    self.player.print_cards()

    if self.check_blackjack():
      print("BLACKJACK!")
      self.player_won(True)
      self.end_of_round()
      return True

    self.dealer.add_card(self.draw_card())
    self.dealer.add_card(self.draw_card())

    self.dealer.print_cards(False)

    return False


  def start_game(self):

    print("Hello, welcome to play Blackjack!")

    while self.player.money > 0:

      got_blackjack = self.start_of_round()

      if got_blackjack:
        continue

      self.player_turn()
      
      if self.player.total > 21:
        self.check_win()
        self.end_of_round()
        continue

      self.dealer_turn()

      print("--------------------\n")

      self.player.print_cards()
      self.dealer.print_cards(True)

      self.check_win()

      self.end_of_round()


if __name__ == "__main__":
  game = Game()
  game.start_game()
  pass
