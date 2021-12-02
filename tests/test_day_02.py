from aoc2021.day_02 import first_task, second_task


def test_first_task() -> None:
    test_program = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

    assert first_task(test_program) == 150


def test_second_task() -> None:
    test_program = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

    assert second_task(test_program) == 900
