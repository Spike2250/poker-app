import pytest

from utils.games.poker import Deck, Suit, Rank, Card


@pytest.fixture()
def full_new_deck():
    return Deck()


@pytest.fixture()
def small_deck():
    return Deck(
        cards=[
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.SIX, suit=Suit.CLUBS),
        ],
    )


def test_deck_print(small_deck):
    assert str(small_deck) == f"{[str(card) for card in small_deck.cards]}"


def test_deck_slice(small_deck):
    deck = small_deck

    assert deck.cards[0] == Card(rank=Rank.JACK, suit=Suit.DIAMONDS)

    deck.slice(3)
    assert deck.cards[0] == Card(rank=Rank.EIGHT, suit=Suit.CLUBS)
    assert deck.cards[-3] == Card(rank=Rank.JACK, suit=Suit.DIAMONDS)
    deck.slice(0)
    assert deck.cards[0] == Card(rank=Rank.EIGHT, suit=Suit.CLUBS)
    assert deck.cards[-3] == Card(rank=Rank.JACK, suit=Suit.DIAMONDS)

    with pytest.raises(ValueError):
        deck.slice(-1)
    with pytest.raises(ValueError):
        deck.slice(6)
    with pytest.raises(ValueError):
        deck.slice(12)

    deck.slice(4)
    assert deck.cards[0] == Card(rank=Rank.ACE, suit=Suit.HEARTS)
    assert deck.cards[1] == Card(rank=Rank.KING, suit=Suit.SPADES)