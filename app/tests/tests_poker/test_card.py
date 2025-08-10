import pytest
import random

from utils.games.poker import (
    Card,
    Suit,
    Rank,
)


def test_rank_strength():
    assert Rank.TWO.strength == 2
    assert Rank.JACK.strength == 11
    assert Rank.ACE.strength == 14
    assert Rank.ACE.strength > Rank.KING.strength
    assert Rank.TWO.strength < Rank.FIVE.strength
    assert Rank.SIX.strength == Rank.SIX.strength


@pytest.mark.parametrize("card, str_card", [
    (
        Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
        'J♦'
    ),
    (
        Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
        '7♥'
    ),
    (
        Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
        'Q♥'
    ),
],)
def test_card(card: Card, str_card: str) -> None:
    """"""
    prev_card_rank = Rank.TWO
    next_card_rank = Rank.TWO
    for i, rank in enumerate(ranks := list(Rank)):
        if rank == card.rank:
            prev_card_rank = ranks[i - 1]
            next_card_rank = ranks[i + 1]
    suits = set(list(Suit))
    suits.remove(card.suit)
    some_another_suit = random.choice(list(suits))
    cards = {
        "prev": Card(
            rank=Rank(prev_card_rank),
            suit=Suit(some_another_suit),
        ),
        "like": Card(
            rank=Rank(card.rank),
            suit=Suit(some_another_suit),
        ),
        "next": Card(
            rank=Rank(next_card_rank),
            suit=Suit(some_another_suit),
        ),
    }

    assert cards['prev'] < cards['like']
    assert cards['next'] > cards['like']
    assert cards['next'] > cards['prev']
    assert cards['next'].strength - cards['like'].strength == 1
    assert cards['next'].strength - cards['prev'].strength == 2

    assert card == cards['like']
    assert card.suit != cards['like'].suit
    assert cards['prev'].suit == cards['like'].suit == cards['next'].suit

    assert str_card == card.__str__()
