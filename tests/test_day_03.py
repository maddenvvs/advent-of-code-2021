from aoc2021.day_03 import (
    first_task,
    second_task,
    oxygen_generator_rating,
    co2_scrubber_rating,
)

TEST_REPORT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def test_first_task() -> None:
    assert first_task(TEST_REPORT) == 198


def test_oxygen_generator_rating() -> None:
    assert oxygen_generator_rating(TEST_REPORT.split("\n")) == 23


def test_co2_scrubber_rating() -> None:
    assert co2_scrubber_rating(TEST_REPORT.split("\n")) == 10


def test_second_task() -> None:
    assert second_task(TEST_REPORT) == 230
