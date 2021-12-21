from typing import Generator
from collections import Counter
from itertools import product
from functools import cache

DIRAC_DICE_OUTCOMES = Counter(sum(p) for p in product((1, 2, 3), repeat=3))


def deterministic_die() -> Generator[int, None, None]:
    side = 0
    while True:
        yield side + 1
        side = (side + 1) % 100


def simulate_deterministic_game(player_1: int, player_2: int) -> tuple[int, int, int]:
    die = deterministic_die()
    pos = [player_1 - 1, player_2 - 1]
    scores = [0, 0]
    turn = 0

    while all(s < 1000 for s in scores):
        moves = sum(next(die) for _ in range(3))
        pos[turn % 2] = (pos[turn % 2] + moves) % 10
        scores[turn % 2] += pos[turn % 2] + 1
        turn += 1

    return scores[0], scores[1], turn


@cache
def winning_universes(
    pos_1: int, score_1: int, pos_2: int, score_2: int
) -> tuple[int, int]:
    if score_1 > 20:
        return (1, 0)

    if score_2 > 20:
        return (0, 1)

    universe_1, universe_2 = 0, 0

    for outcome, amount in DIRAC_DICE_OUTCOMES.items():
        new_pos_1 = (pos_1 + outcome) % 10
        new_score_1 = score_1 + new_pos_1 + 1

        first, second = winning_universes(pos_2, score_2, new_pos_1, new_score_1)
        universe_1 += amount * second
        universe_2 += amount * first

    return universe_1, universe_2


def parse_player_position(player: str) -> int:
    return int(player.split()[-1])


def parse_players(players: str) -> tuple[int, int]:
    first, second = players.split("\n")
    return parse_player_position(first), parse_player_position(second)


def first_task(players: str) -> int:
    first, second = parse_players(players)
    first_score, second_score, turns = simulate_deterministic_game(first, second)
    return min(first_score, second_score) * turns * 3


def second_task(players: str) -> int:
    first, second = parse_players(players)
    return max(winning_universes(first - 1, 0, second - 1, 0))
