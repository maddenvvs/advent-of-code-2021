from aoc2021.day_01 import first_task, second_task


def test_first_task() -> None:
    test_entries = """199
200
208
210
200
207
240
269
260
263"""

    assert first_task(test_entries) == 7


def test_second_task() -> None:
    test_entries = """199
200
208
210
200
207
240
269
260
263"""

    assert second_task(test_entries) == 5
