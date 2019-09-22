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
      return "{}(1)".format(self.value)
    else:
      return str(self.value)