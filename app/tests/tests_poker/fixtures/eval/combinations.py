from utils.games.poker import (
    Card,
    Rank,
    Suit,
    HandEvaluation,
    HandRank,
)


combinations = [
    (
        [
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
        ],
        HandEvaluation(
            rank=HandRank.royal_flush,
            primary=[14],
        )
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
        [
            Card(rank=Rank.NINE, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.JACK, suit=Suit.CLUBS),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
        ],
        HandEvaluation(
            rank=HandRank.straight_flush,
            primary=[13],
        )
    ),
    # == == == == == == == == == == == == == == == ==
    (
        [
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
        ],
        [
            Card(rank=Rank.NINE, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.ACE, suit=Suit.CLUBS),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.SPADES),
        ],
        HandEvaluation(
            rank=HandRank.full_house,
            primary=[13],
            kickers=[14],
        )
    ),
    # == == == == == == == == == == == == == == == ==
]
