regions = {
  1: "♠", 
  2: "♦", 
  3: "♥", 
  4: "♣"
}

values = {
  "2": "2",
  "3": "3",
  "4": "4",
  "5": "5",
  "6": "6",
  "7": "7",
  "8": "8",
  "9": "9",
  "10": "10",
  "11": "8",

}

class Card:

  def __init__(self, region, value):
    self.region = region
    if value == 14:
      self.value = 11
    elif value > 10:
      self.value = 10
    else:
      self.value = value

  def __str__(self):
    if self.value == 14:
      # if self.value == 14:
      #   space = " "

      # elif self.value > 10:

      # else:
      #   space = " "

      # "┌─────────┐\n"
      # "│{}{}       │\n".format(self.value, space)) + # use two {} one for char, one for space or char
      # "│         │\n" +
      # "│         │\n" +
      # "│    {}    │\n".format(self.region))
      # "│         │\n" +
      # "│         │\n" +
      # "│       {}{}\n│".format(space, self.value)) +
      # "└─────────┘\n" 

      return "{}(1)".format(self.value)
    else:
      return str(self.value)
