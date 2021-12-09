from aoc2021.day_09 import first_task, second_task

TEST_HEIGHTMAP = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def test_first_task() -> None:
    assert first_task(TEST_HEIGHTMAP) == 15


def test_second_task() -> None:
    assert second_task(TEST_HEIGHTMAP) == 1134
