import unittest

from Game import Game, NUMBER_OF_DECKS
from Player import Player

class TestGame(unittest.TestCase):

    def test_draw_card(self):
      test_game = Game()
      test_game.draw_card()

      self.assertEqual(len(test_game.cards), (NUMBER_OF_DECKS * 4 * 13) - 1, "Should remove the card when it is drawn")

    def test_check_win(self):
      test_game = Game()

      test_player = Player(100, "player")
      test_dealer = Player(0, "dealer")

      test_game.player = test_player
      test_game.dealer = test_dealer

      test_player.total = 20
      test_dealer.total = 19

      self.player_won = False
      self.called = 0
      def mock_player_won(_):
        self.player_won = True
        self.called += 1

      test_game.player_won = mock_player_won
      test_game.check_win()


      self.assertEqual(self.player_won, True, "Player should win when player total is 20 and dealer total is 19")

      test_player.total = 19
      test_dealer.total = 20

      self.player_won = False
      test_game.check_win()

      self.assertEqual(self.player_won, False, "Player should lose when player total is 19 and dealer total is 20")

      test_player.total = 25
      test_dealer.total = 20

      self.player_won = False
      test_game.check_win()

      self.assertEqual(self.player_won, False, "Player should lose when player total is 25 and dealer total is 20")

      test_player.total = 20
      test_dealer.total = 25

      self.player_won = False
      test_game.check_win()

      self.assertEqual(self.player_won, True, "Player should win when player total is 20 and dealer total is 25")
    
