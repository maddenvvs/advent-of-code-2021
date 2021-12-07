from aoc2021.day_07 import first_task, second_task

TEST_CRABS = """16,1,2,0,4,2,7,1,2,14"""


def test_first_task() -> None:
    assert first_task(TEST_CRABS) == 37


def test_second_task() -> None:
    assert second_task(TEST_CRABS) == 168
