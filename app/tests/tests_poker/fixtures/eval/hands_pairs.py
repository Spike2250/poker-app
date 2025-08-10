from utils.games.poker import (
    Card,
    Rank,
    Suit,
)


hands_pairs = [
    (
        [
            Card(rank=Rank.NINE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.NINE, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.NINE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.HEARTS),
            Card(rank=Rank.FOUR, suit=Suit.HEARTS),
            Card(rank=Rank.FIVE, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.NINE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TWO, suit=Suit.CLUBS),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.SIX, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.THREE, suit=Suit.HEARTS),
            Card(rank=Rank.FOUR, suit=Suit.HEARTS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.FIVE, suit=Suit.HEARTS),
            Card(rank=Rank.SIX, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.NINE, suit=Suit.CLUBS),
            Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
            Card(rank=Rank.NINE, suit=Suit.HEARTS),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.KING, suit=Suit.CLUBS),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TWO, suit=Suit.CLUBS),
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.THREE, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.THREE, suit=Suit.CLUBS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.THREE, suit=Suit.HEARTS),
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.EIGHT, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.THREE, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.THREE, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.FIVE, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.FIVE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.FIVE, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.FIVE, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.FIVE, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.FIVE, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.FIVE, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.FIVE, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.CLUBS),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.FIVE, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.FOUR, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.FOUR, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.KING, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.TWO, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.FOUR, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
        ],
        [
            Card(rank=Rank.TEN, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
        ],
    ),
    # == == == == == == == == == == == == == == == ==
]