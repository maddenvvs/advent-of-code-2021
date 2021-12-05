from aoc2021.day_02 import first_task, second_task

TEST_PROGRAM = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def test_first_task() -> None:
    assert first_task(TEST_PROGRAM) == 150


def test_second_task() -> None:
    assert second_task(TEST_PROGRAM) == 900
