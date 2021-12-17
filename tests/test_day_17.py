from aoc2021.day_17 import first_task, second_task

TEST_TARGET_AREA = """target area: x=20..30, y=-10..-5"""


def test_first_task() -> None:
    assert first_task(TEST_TARGET_AREA) == 45


def test_second_task() -> None:
    assert second_task(TEST_TARGET_AREA) == 112
