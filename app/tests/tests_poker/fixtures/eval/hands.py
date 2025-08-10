from utils.games.poker import (
    Card,
    Rank,
    Suit,
    HandRank,
    HandEvaluation,
)


hands = [
    # Royal Flash
    (
        [
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ],
        HandEvaluation(
            rank=HandRank.royal_flush,
            primary=[14],
        )
    ),
    # Straight Flash (1 - 3)
    (
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
    (
        [
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
            Card(rank=Rank.EIGHT, suit=Suit.SPADES),
        ],
        HandEvaluation(
            rank=HandRank.straight_flush,
            primary=[12],
        )
    ),
    (
        [
            Card(rank=Rank.ACE, suit=Suit.DIAMONDS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            Card(rank=Rank.FOUR, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.straight_flush,
            primary=[5],
            hand=[
                Card(rank=Rank.ACE, suit=Suit.DIAMONDS),
                Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
                Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
                Card(rank=Rank.FOUR, suit=Suit.DIAMONDS),
                Card(rank=Rank.FIVE, suit=Suit.DIAMONDS),
            ],
        )
    ),
    # Quad (4 - 5)
    (
        [
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.JACK, suit=Suit.CLUBS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.EIGHT, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.four_of_a_kind,
            primary=[11],
            kickers=[8],
        )
    ),
    (
        [
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.CLUBS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
        ],
        HandEvaluation(
            rank=HandRank.four_of_a_kind,
            primary=[2],
            kickers=[14],
        )
    ),
    # Full House (6 - 8)
    (
        [
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
        ],
        HandEvaluation(
            rank=HandRank.full_house,
            primary=[12],
            kickers=[14],
        )
    ),
    (
        [
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
        ],
        HandEvaluation(
            rank=HandRank.full_house,
            primary=[13],
            kickers=[7],
        )
    ),
    (
        [
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.THREE, suit=Suit.CLUBS),
            Card(rank=Rank.THREE, suit=Suit.SPADES),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
        ],
        HandEvaluation(
            rank=HandRank.full_house,
            primary=[3],
            kickers=[2],
        )
    ),
    # Flash (9 - 11)
    (
        [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.SPADES),
            Card(rank=Rank.FOUR, suit=Suit.SPADES),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
        ],
        HandEvaluation(
            rank=HandRank.flush,
            primary=[13, 11, 9, 5, 4],
        )
    ),
    (
        [
            Card(rank=Rank.ACE, suit=Suit.CLUBS),
            Card(rank=Rank.SEVEN, suit=Suit.CLUBS),
            Card(rank=Rank.FIVE, suit=Suit.CLUBS),
            Card(rank=Rank.FOUR, suit=Suit.CLUBS),
            Card(rank=Rank.TWO, suit=Suit.CLUBS),
        ],
        HandEvaluation(
            rank=HandRank.flush,
            primary=[14, 7, 5, 4, 2],
        )
    ),
    (
        [
            Card(rank=Rank.SIX, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.FIVE, suit=Suit.HEARTS),
            Card(rank=Rank.FOUR, suit=Suit.HEARTS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
        ],
        HandEvaluation(
            rank=HandRank.flush,
            primary=[10, 6, 5, 4, 2],
        )
    ),
    # Straight (12 - 14)
    (
        [
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.EIGHT, suit=Suit.HEARTS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
            Card(rank=Rank.SIX, suit=Suit.CLUBS),
        ],
        HandEvaluation(
            rank=HandRank.straight,
            primary=[10],
        )
    ),
    (
        [
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.CLUBS),
            Card(rank=Rank.EIGHT, suit=Suit.HEARTS),
            Card(rank=Rank.SEVEN, suit=Suit.HEARTS),
        ],
        HandEvaluation(
            rank=HandRank.straight,
            primary=[11],
        )
    ),
    (
        [
            Card(rank=Rank.ACE, suit=Suit.CLUBS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.FIVE, suit=Suit.HEARTS),
            Card(rank=Rank.FOUR, suit=Suit.CLUBS),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.straight,
            primary=[5],
            hand=[
                Card(rank=Rank.ACE, suit=Suit.CLUBS),
                Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
                Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
                Card(rank=Rank.FOUR, suit=Suit.CLUBS),
                Card(rank=Rank.FIVE, suit=Suit.HEARTS),
            ],
        )
    ),
    # Three of a kind (15 - 17)
    (
        [
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
            Card(rank=Rank.TEN, suit=Suit.HEARTS),
            Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.three_of_a_kind,
            primary=[10],
            kickers=[11, 8]
        )
    ),
    (
        [
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
            Card(rank=Rank.EIGHT, suit=Suit.HEARTS),
            Card(rank=Rank.EIGHT, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.three_of_a_kind,
            primary=[8],
            kickers=[11, 10]
        )
    ),
    (
        [
            Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.THREE, suit=Suit.CLUBS),
            Card(rank=Rank.THREE, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.three_of_a_kind,
            primary=[3],
            kickers=[9, 2]
        )
    ),
    # Two pairs (18 - 20)
    (
        [
            Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.SPADES),
            Card(rank=Rank.THREE, suit=Suit.CLUBS),
            Card(rank=Rank.NINE, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.two_pair,
            primary=[9, 3],
            kickers=[2]
        )
    ),
    (
        [
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.two_pair,
            primary=[12, 11],
            kickers=[14]
        )
    ),
    (
        [
            Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.SIX, suit=Suit.CLUBS),
            Card(rank=Rank.SIX, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.two_pair,
            primary=[10, 6],
            kickers=[14]
        )
    ),
    # One Pair (21 - 23)
    (
        [
            Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.TEN, suit=Suit.CLUBS),
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.SIX, suit=Suit.CLUBS),
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.one_pair,
            primary=[10],
            kickers=[14, 6, 2]
        )
    ),
    (
        [
            Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.SIX, suit=Suit.CLUBS),
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.one_pair,
            primary=[2],
            kickers=[12, 11, 6]
        )
    ),
    (
        [
            Card(rank=Rank.EIGHT, suit=Suit.DIAMONDS),
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
            Card(rank=Rank.SEVEN, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.one_pair,
            primary=[8],
            kickers=[13, 12, 7]
        )
    ),
    # High Card (24 - 28)
    (
        [
            Card(rank=Rank.EIGHT, suit=Suit.DIAMONDS),
            Card(rank=Rank.FOUR, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
            Card(rank=Rank.SEVEN, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.high_card,
            primary=[13],
            kickers=[12, 8, 7, 4]
        )
    ),
    (
        [
            Card(rank=Rank.EIGHT, suit=Suit.DIAMONDS),
            Card(rank=Rank.FOUR, suit=Suit.CLUBS),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.THREE, suit=Suit.CLUBS),
            Card(rank=Rank.SEVEN, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.high_card,
            primary=[12],
            kickers=[8, 7, 4, 3]
        )
    ),
    (
        [
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.FIVE, suit=Suit.CLUBS),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.CLUBS),
            Card(rank=Rank.SEVEN, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.high_card,
            primary=[14],
            kickers=[11, 7, 5, 3]
        )
    ),
    (
        [
            Card(rank=Rank.SIX, suit=Suit.DIAMONDS),
            Card(rank=Rank.FIVE, suit=Suit.CLUBS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.CLUBS),
            Card(rank=Rank.SEVEN, suit=Suit.DIAMONDS),
        ],
        HandEvaluation(
            rank=HandRank.high_card,
            primary=[7],
            kickers=[6, 5, 3, 2]
        )
    ),
    (
        [
            Card(rank=Rank.NINE, suit=Suit.SPADES),
            Card(rank=Rank.FIVE, suit=Suit.CLUBS),
            Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.FOUR, suit=Suit.CLUBS),
        ],
        HandEvaluation(
            rank=HandRank.high_card,
            primary=[10],
            kickers=[9, 5, 4, 2]
        )
    ),
]
