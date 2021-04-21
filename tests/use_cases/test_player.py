import unittest

from src.entities.player import Player, NotEnoughMoney
from src.entities.deck import Card


class TestPlayer(unittest.TestCase):

    INITIAL_MONEY = 100.0

    def test_when_retrieving_money_then_money_is_reduced(self):
        player = Player(money=self.INITIAL_MONEY)

        money_retrieved = 10
        player.retrieve_money(money_retrieved)

        self.assertEqual(player.money,
                         self.INITIAL_MONEY - money_retrieved)

    def test_when_there_is_not_enough_money_to_retrieve_then_it_fails(self):
        player = Player(money=0)

        self.assertRaises(NotEnoughMoney, player.retrieve_money, 10)

    def test_when_adding_money_then_money_is_added(self):
        player = Player(money=self.INITIAL_MONEY)

        money_added = 10
        player.add_money(money_added)

        self.assertEqual(player.money,
                         self.INITIAL_MONEY + money_added)
