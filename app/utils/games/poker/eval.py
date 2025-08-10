from enum import Enum
from itertools import combinations
from collections import Counter
from typing import List, Sequence

from pydantic import BaseModel

from .card import Card


class HandRank(int, Enum):
    royal_flush: int = 9
    straight_flush: int = 8
    four_of_a_kind: int = 7
    full_house: int = 6
    flush: int = 5
    straight: int = 4
    three_of_a_kind: int = 3
    two_pair: int = 2
    one_pair: int = 1
    high_card: int = 0


class HandEvaluation(BaseModel):
    rank: HandRank
    primary: List[int]
    kickers: List[int] = []
    hand: List[Card] | None = None

    @property
    def _comparison_tuple(self) -> tuple:
        """Кортеж для сравнения силы руки"""
        return (
            self.rank.value,
            self.primary,
            self.kickers
        )

    def __lt__(self, other) -> bool:
        return self._comparison_tuple < other._comparison_tuple

    def __eq__(self, other) -> bool:
        return self._comparison_tuple == other._comparison_tuple

    def __str__(self):
        return f"{self.rank.name} - {[str(card) for card in self.hand]}"


def evaluate_hand(cards: List[Card]) -> HandEvaluation:
    """
    TODO: ограничить длину списка cards - 5 картами
    """
    sorted_cards = sorted(cards, reverse=True)
    ranks = [card.strength for card in sorted_cards]
    suits = [card.suit for card in sorted_cards]

    # Проверка на flush и straight
    flush = len(set(suits)) == 1
    minor_straight = set(ranks) == {14, 2, 3, 4, 5}
    straight = (
        max(ranks) - min(ranks) == 4
        and len(set(ranks)) == 5
    ) or minor_straight

    # Royal и Straight Flush
    if flush and straight:
        if max(ranks) == 14:
            if not minor_straight:
                return HandEvaluation(
                    rank=HandRank.royal_flush,
                    primary=[14],
                    kickers=[],
                    hand=sorted_cards,
                )
            else:
                return HandEvaluation(
                    rank=HandRank.straight_flush,
                    primary=[5],
                    kickers=[],
                    hand=[sorted_cards[0]] + sorted(cards, reverse=False)[:-1],
                )
        return HandEvaluation(
                    rank=HandRank.straight_flush,
                    primary=[max(ranks)],
                    kickers=[],
                    hand=sorted_cards,
                )

    # Группировка по рангам
    count = Counter(ranks)
    grouped = sorted(count.items(), key=lambda x: (-x[1], -x[0]))
    values = [item[0] for item in grouped]
    counts = [item[1] for item in grouped]

    # Four of a Kind
    if 4 in counts:
        return HandEvaluation(
            rank=HandRank.four_of_a_kind,
            primary=[values[0]],
            kickers=[max(set(ranks) - {values[0]})],
            hand=sorted_cards,
        )

    # Full House
    if 3 in counts and 2 in counts:
        return HandEvaluation(
            rank=HandRank.full_house,
            primary=[values[0]],
            kickers=[values[1]],
            hand=sorted_cards,
        )

    # Flush
    if flush:
        return HandEvaluation(
            rank=HandRank.flush,
            primary=ranks,
            kickers=[],
            hand=sorted_cards,
        )

    # Straight
    if straight:
        if set(ranks) == {14, 2, 3, 4, 5}:
            high = 5
            hand = [sorted_cards[0]] + sorted(cards, reverse=False)[:-1]
        else:
            high = max(ranks)
            hand = sorted_cards
        return HandEvaluation(
            rank=HandRank.straight,
            primary=[high],
            kickers=[],
            hand=hand,
        )

    # Three of a Kind
    if 3 in counts:
        triplet = values[0]
        kickers = sorted(set(ranks) - {triplet}, reverse=True)
        return HandEvaluation(
            rank=HandRank.three_of_a_kind,
            primary=[triplet],
            kickers=kickers,
            hand=sorted_cards,
        )

    # Two Pair
    if counts.count(2) == 2:
        pairs = [v for v, c in count.items() if c == 2]
        kickers = sorted(set(ranks) - set(pairs), reverse=True)[:1]
        return HandEvaluation(
            rank=HandRank.two_pair,
            primary=pairs,
            kickers=kickers,
            hand=sorted_cards,
        )

    # One Pair
    if 2 in counts:
        pair = values[0]
        kickers = sorted(set(ranks) - {pair}, reverse=True)[:3]
        return HandEvaluation(
            rank=HandRank.one_pair,
            primary=[pair],
            kickers=kickers,
            hand=sorted_cards,
        )

    # High Card
    return HandEvaluation(
        rank=HandRank.high_card,
        primary=[ranks[0]],
        kickers=ranks[1:5],
        hand=sorted_cards,
    )


def get_best_hand(
    player_hand: List[Card],
    community: List[Card]
) -> HandEvaluation:
    all_cards = player_hand + community
    possible_hands = combinations(list(range(len(all_cards))), 5)

    def get_cards_from_ids(ids: Sequence[int]) -> List[Card]:
        return [all_cards[id] for id in ids]

    possible_hands = [get_cards_from_ids(ids) for ids in list(possible_hands)]
    return max([evaluate_hand(hand) for hand in possible_hands])
