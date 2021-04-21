from dataclasses import dataclass

from src.entities.blind import Blind
from src.entities.deck import Card


class NotEnoughMoney(Exception):
    pass


@dataclass
class Player:
    id: int
    is_dealer: bool
    blind: Blind
    money: float
    hand: [Card]

    def __init__(self, money=0):
        self.money = money

    def retrieve_money(self, n):
        future_money = self.money - n
        if future_money < 0:
            raise NotEnoughMoney("Player does not have enough money")
        self.money = future_money

    def add_money(self, n):
        self.money = self.money + n
