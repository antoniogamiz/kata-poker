from dataclasses import dataclass, field

from entities.blind import Blind
from entities.deck import Card


class NotEnoughMoney(Exception):
    pass


@dataclass
class Player:
    id: int
    is_dealer: bool = False
    blind: Blind = None
    money: float = 0
    hand: [Card] = field(default_factory=list)

    def retrieve_money(self, n):
        future_money = self.money - n
        if future_money < 0:
            raise NotEnoughMoney("Player does not have enough money")
        self.money = future_money

    def add_money(self, n):
        self.money = self.money + n
