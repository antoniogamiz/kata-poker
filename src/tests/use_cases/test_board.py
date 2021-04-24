import unittest

from entities.player import Player
from entities.blind import Blind
from use_cases.board import Board, NoPlayersFound, NoEnoughPlayers


class TestBoard(unittest.TestCase):

    HAND_CARD_NUMBER = 5

    def test_when_game_is_started_without_players_then_it_fails(self):
        board = Board()

        self.assertRaises(NoPlayersFound, board.start_game)

    def test_when_game_is_started_without_enough_players_then_it_fails(self):
        board = Board()
        board.players = [self._create_players()[0]]

        self.assertRaises(NoEnoughPlayers, board.start_game)

    def test_when_game_is_started_then_blinds_and_dealer_are_assigned(self):
        board = Board()
        board.players = self._create_players()

        board.start_game()

        self._assert_dealer_setting(board, [True, False, False])
        self._assert_blind_setting(board, [Blind.NONE, Blind.SMALL, Blind.BIG])

    def test_when_game_is_started_then_round_number_is_set_to_zero(self):
        board = Board()
        board.players = self._create_players()

        board.start_game()

        self.assertEqual(board.round_number, 0)

    def test_when_next_round_then_round_number_is_increased(self):
        board = Board()
        board.players = self._create_players()

        board.start_game()
        board.next_round()

        self.assertEqual(board.round_number, 1)

    def test_when_next_round_then_dealer_and_blinds_are_set(self):
        board = Board()
        board.players = self._create_players()

        board.start_game()
        board.next_round()

        self._assert_dealer_setting(board, [False, True, False])
        self._assert_blind_setting(board, [Blind.BIG, Blind.NONE, Blind.SMALL])

    def test_when_cards_are_dealed_then_players_receive_them(self):
        board = Board()
        board.players = self._create_players()
        board.start_game()

        board.deal_cards()

        for player in board.players:
            self.assertEqual(len(player.cards), self.HAND_CARD_NUMBER)

    def _create_players(self):
        player1 = Player(id=0)
        player2 = Player(id=1)
        player3 = Player(id=2)
        return [player1, player2, player3]

    def _assert_dealer_setting(self, board, settings):
        for i, player in enumerate(board.players):
            self.assertEqual(player.is_dealer, settings[i])

    def _assert_blind_setting(self, board, settings):
        for i, player in enumerate(board.players):
            self.assertEqual(player.blind, settings[i])
