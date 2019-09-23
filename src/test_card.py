import unittest

from Card import Card

class TestCard(unittest.TestCase):

    def test_render(self):
      card_value = 7
      card = Card(0, card_value, card_value)
      card_ascii = [
        " _________ ",
        "|7        |", 
        "|         |",
        "|         |",
        "|    ^    |",
        "|         |",
        "|         |",
        "|________7|",
      ]
      self.assertEqual(card.__str__(), card_ascii, "Card should render reference Ascii")

    def test_special_card(self):
      card_value = 11
      card = Card(0, card_value, card_value)

      self.assertEqual(card.value, 10, "Jack should have value 10")

      card_value = 12
      card = Card(0, card_value, card_value)

      self.assertEqual(card.value, 10, "Queen should have value 10")

      card_value = 13
      card = Card(0, card_value, card_value)

      self.assertEqual(card.value, 10, "King should have value 10")

      card_value = 14
      card = Card(0, card_value, card_value)

      self.assertEqual(card.value, 11, "Ace should have value 11")

if __name__ == '__main__':
  unittest.main()
  