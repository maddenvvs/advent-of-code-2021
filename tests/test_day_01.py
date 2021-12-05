from aoc2021.day_01 import first_task, second_task

TEST_ENTRIES = """199
200
208
210
200
207
240
269
260
263"""


def test_first_task() -> None:
    assert first_task(TEST_ENTRIES) == 7


def test_second_task() -> None:
    assert second_task(TEST_ENTRIES) == 5
