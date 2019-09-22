class Player:
  def __init__(self, start_money):
    self.money = start_money
    self.cards = []
    self.current_bet = 0
    self.total = 0

  def add_card(self, card):
    self.cards.append(card)
    self.total += card.value
    
    has_14 = False
    for card in self.cards:
      if card.value == 14:
        has_14 = True
        break

    if (card.value == 14 or has_14) and self.total > 21:
      self.total -= 13

  def add_win(self, win_multiplier):
    self.money += (self.current_bet * win_multiplier)

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
    
    self.current_bet = bet_amount
    return bet_amount

  def print_cards(self):
    print("Your cards: ")
    total = 0
    for card in self.cards:
      print(card, end=" ")
    print("Total: {}".format(self.total), end=" ")
    print("")