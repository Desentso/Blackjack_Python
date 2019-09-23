regions = {
  0: "^", #"♠", 
  1: "o", #"♦", 
  2: "v", #"♥", 
  3: "&", #"♣"
}

values = {
  1: "A",
  2: "2",
  3: "3",
  4: "4",
  5: "5",
  6: "6",
  7: "7",
  8: "8",
  9: "9",
  10: "10",
  11: "J",
  12: "Q",
  13: "K",
  14: "A"
}

# Prints cards line by line, so that they appear next to each other, instead of on top of each other
def print_cards(cards, has_hidden_card = False):
  card_strs = []

  for card in cards:
    card_strs.append(card.__str__())

  if has_hidden_card:
    card_strs.append([
      " _________ ",
      "|---------|", 
      "|---------|",
      "|---------|",
      "|---------|",
      "|---------|",
      "|---------|",
      "|_________|",
    ])

  for i in range(8):
    for card in card_strs:
      print(card[i], end=" ")

    print("")

class Card:

  def __init__(self, region, value, key):
    self.region = region
    if value == 14:
      self.value = 11
    elif value > 10:
      self.value = 10
    else:
      self.value = value
    self.key = key

  def __str__(self):
    space = "_"
    space_first = " "

    if self.key == 10:
      space = ""
      space_first = ""

    lines = []
    lines.append(" _________ ")
    lines.append("|{}{}       |".format(values[self.key], space_first)) 
    lines.append("|         |")
    lines.append("|         |")
    lines.append("|    {}    |".format(regions[self.region]))
    lines.append("|         |")
    lines.append("|         |")
    lines.append("|_______{}{}|".format(space, values[self.key]))

    return lines
