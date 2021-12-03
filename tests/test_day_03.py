from aoc2021.day_03 import (
    first_task,
    second_task,
    oxygen_generator_rating,
    co2_scrubber_rating,
)


def test_first_task() -> None:
    test_report = """00100
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

    assert first_task(test_report) == 198


def test_oxygen_generator_rating() -> None:
    test_report = """00100
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
01010""".split(
        "\n"
    )

    assert oxygen_generator_rating(test_report) == 23


def test_co2_scrubber_rating() -> None:
    test_report = """00100
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
01010""".split(
        "\n"
    )

    assert co2_scrubber_rating(test_report) == 10


def test_second_task() -> None:
    test_report = """00100
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

    assert second_task(test_report) == 230
