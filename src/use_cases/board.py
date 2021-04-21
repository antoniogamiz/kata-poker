from src.use_cases.dealer import Dealer
from src.entities.player import Player
from src.entities.blind import Blind


class Board:
    dealer: Dealer
    round_number: int
    players: [Player]

    HAND_CARD_NUMBER = 5

    def __init__(self):
        self.players = []

    def start_game(self):
        self.dealer = Dealer()
        self.round_number = 0
        if not self.players:
            raise NoPlayersFound("No players have been found.")
        if len(self.players) < 3:
            raise NoEnoughPlayers(
                "You need at least 3 players to start a game")
        self._set_dealer()
        self._set_blinds()

    def _set_dealer(self):
        number_of_players = len(self.players)
        previous_dealer_index = (self.round_number - 1) % number_of_players
        current_dealer_index = self.round_number % number_of_players
        self.players[previous_dealer_index].is_dealer = False
        self.players[current_dealer_index].is_dealer = True

    def _set_blinds(self):
        dealer_index = self._get_dealer_index()
        number_of_players = len(self.players)
        small_blind_index = (self.round_number + 1) % number_of_players
        big_blind_index = (self.round_number + 2) % number_of_players
        self.players[dealer_index].blind = Blind.NONE
        self.players[small_blind_index].blind = Blind.SMALL
        self.players[big_blind_index].blind = Blind.BIG

    def _get_dealer_index(self):
        return next((i for i, player in enumerate(self.players) if player.is_dealer == True), -1)

    def next_round(self):
        self.round_number = self.round_number + 1
        self._set_dealer()
        self._set_blinds()

    def deal_cards(self):
        for player in self.players:
            player.cards = self.dealer.next_cards(self.HAND_CARD_NUMBER)


class NoPlayersFound(Exception):
    pass


class NoEnoughPlayers(Exception):
    pass
