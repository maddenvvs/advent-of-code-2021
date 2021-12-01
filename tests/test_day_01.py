from aoc2021.solutions.day_01 import first_task, second_task, parse_entries


def test_first_task():
    test_entries = parse_entries(
        """199
200
208
210
200
207
240
269
260
263"""
    )

    assert first_task(test_entries) == 7


def test_second_task():
    test_entries = parse_entries(
        """199
200
208
210
200
207
240
269
260
263"""
    )

    assert second_task(test_entries) == 5
