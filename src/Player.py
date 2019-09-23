from Card import print_cards

class Player:
  def __init__(self, start_money, player_type):
    self.money = start_money
    self.cards = []
    self.current_bet = 0
    self.total = 0
    self.player_type = player_type

  def reset(self):
    self.cards = []
    self.current_bet = 0
    self.total = 0

  def add_card(self, card):
    self.cards.append(card)
    self.total += card.value
    
    has_11 = False
    for card in self.cards:
      if card.value == 11:
        has_11 = card
        break

    if card.value == 11 and self.total > 21:
      card.value = 1
      self.total -= 10
    elif has_11 and self.total > 21:
      has_11.value = 1
      self.total -= 10

  def add_win(self, win_multiplier):
    self.money += int(self.current_bet * win_multiplier)

  def ask_for_bet(self):
    print("You have {} coins, how much would you like to bet?".format(self.money))
    bet_amount = 0

    while bet_amount <= 0 or bet_amount > self.money:
      print("Please enter a number between 1-{}.".format(self.money))
      try:
        bet_amount = int(input())
      except Exception:
        bet_amount = 0
        pass
    
    self.money -= bet_amount
    self.current_bet = bet_amount
    return bet_amount

  def print_cards(self, show_2 = True):
    if self.player_type == "player":
      print("Your cards: ")
    else:
      print("Dealer's cards: ")

    if len(self.cards) == 2 and not show_2:
      print_cards(self.cards[0:1], True)
    else:
      print_cards(self.cards)
      print("Total: {}".format(self.total), end=" ")

    print("\n")
