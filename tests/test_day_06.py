import pytest
from aoc2021.day_06 import first_task, second_task, number_of_fishes, parse_fishes

TEST_FISHES = """3,4,3,1,2"""


@pytest.mark.parametrize(
    "days,expected",
    [
        (1, 5),
        (2, 6),
        (3, 7),
        (4, 9),
        (5, 10),
        (6, 10),
        (7, 10),
        (8, 10),
        (9, 11),
        (10, 12),
        (11, 15),
        (12, 17),
        (13, 19),
        (14, 20),
        (15, 20),
        (16, 21),
        (17, 22),
        (18, 26),
    ],
)
def test_number_of_fishes(days: int, expected_fishes: int) -> None:
    assert number_of_fishes(parse_fishes(TEST_FISHES), days) == expected_fishes


def test_first_task() -> None:
    assert first_task(TEST_FISHES) == 5934


def test_second_task() -> None:
    assert second_task(TEST_FISHES) == 26984457539
