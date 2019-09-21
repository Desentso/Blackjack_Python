class Card:

  def __init__(self, region, value):
    self.region = region
    self.value = value

  def __str__(self):
    if self.value == 13:
      return "{}(1)".format(self.value)
    else:
      return str(self.value)