from aoc2021.day_21 import first_task, second_task

TEST_PLAYERS = """Player 1 starting position: 4
Player 2 starting position: 8"""


def test_first_task() -> None:
    assert first_task(TEST_PLAYERS) == 739785


def test_second_task() -> None:
    assert second_task(TEST_PLAYERS) == 444356092776315
