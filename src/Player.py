class Player:
  def __init__(self, start_money):
    self.money = start_money
    self.cards = []
    self.current_bet = 0

  def add_card(self, card):
    self.cards.append(card)

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
    for card in self.cards:
      print(card, end=" ")