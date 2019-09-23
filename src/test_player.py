import unittest

from Card import Card
from Player import Player

class TestCard(unittest.TestCase):

    def test_add_card(self):
      test_card = Card(0, 8, 8)
      test_player = Player(0, "player")

      test_player.add_card(test_card)

      self.assertIn(test_card, test_player.cards, "Newly added card should be in player's cards")

    def test_reset(self):
      test_card = Card(0, 8, 8)
      test_card2 = Card(2, 11, 11)
      test_player = Player(0, "player")

      test_player.add_card(test_card)
      test_player.add_card(test_card2)
      
      test_player.reset()

      self.assertEqual(len(test_player.cards), 0, "Cards should be reset")
      self.assertEqual(test_player.total, 0, "Total should be reset")
      self.assertEqual(test_player.current_bet, 0, "Current bet should be reset")

    
