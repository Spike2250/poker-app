import pytest

import random
import copy

from utils.games.poker import Suit, Rank, Card, evaluate_hand, get_best_hand

from .fixtures.eval import hands, hands_pairs, combinations


@pytest.mark.parametrize("hand, eval", hands)
def test_hand_eval(hand, eval):
    # тест на равенство
    assert evaluate_hand(hand) == eval

    new_hand = copy.deepcopy(hand)

    def get_random_card(idx: int):
        suits = set(list(Suit)) - {new_hand[idx].suit}
        ranks = set(list(Rank)) - {new_hand[idx].rank}
        return Card(
            suit=random.choice(list(suits)),
            rank=random.choice(list(ranks)),
        )

    # тест на неравенство
    for i, card in enumerate(new_hand):
        new_hand[i] = get_random_card(i)
        if evaluate_hand(new_hand) != eval:
            assert evaluate_hand(new_hand) != eval


@pytest.mark.parametrize("hand_1, hand_2", hands_pairs)
def test_hand_eval_pairs(hand_1, hand_2):
    assert evaluate_hand(hand_1) < evaluate_hand(hand_2)


@pytest.mark.parametrize("player_hand, community_cards, best_eval", combinations)
def test_get_best_hand(player_hand, community_cards, best_eval):
    assert get_best_hand(player_hand, community_cards) == best_eval
