import random
# from typing import Literal

from pydantic import BaseModel

from .card import Card, Suit, Rank


class Deck(BaseModel):
    """Модель колоды карт"""
    cards: list[Card] = []

    def __init__(self, **data):
        super().__init__(**data)
        if not self.cards:
            self.create_new_deck()

    def create_new_deck(self):
        self.cards = [
            Card(suit=suit, rank=rank)
            for rank in Rank
            for suit in Suit
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    @property
    def size(self):
        return len(self.cards)

    def slice(self, card_number: int):
        if 0 <= card_number < self.size:
            self.cards = self.cards[card_number:] + self.cards[:card_number]
        else:
            raise ValueError('Card number must be in "[ 0, len(self.cards) )" diapason')

    def refresh(self):
        self.create_new_deck()
        self.shuffle()

    def draw(self, count: int = 1) -> list[Card]:
        drawn = self.cards[:count]
        self.cards = self.cards[count:]
        return drawn

    def get_preflop_cards(
        self,
        players_number: int,
        cards_count: int = 2,
    ) -> list[list[Card, Card]]:
        hands = [[] for _ in range(players_number)]
        for _ in range(cards_count):
            for i in range(players_number):
                hands[i] += self.draw()
        return hands

    def burn_card(self) -> None:
        self.cards = self.cards[1:]

    def burn_and_draw_one_card(self) -> list[Card]:
        self.burn_card()
        return self.draw()

    def get_flop(self) -> list[Card]:
        self.burn_card()
        return self.draw(3)

    def get_turn(self) -> list[Card]:
        return self.burn_and_draw_one_card()

    def get_river(self) -> list[Card]:
        return self.burn_and_draw_one_card()

    def __len__(self) -> int:
        return len(self.cards)

    def __str__(self) -> str:
        return f"{[str(card) for card in self.cards]}"
