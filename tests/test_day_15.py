from aoc2021.day_15 import first_task, second_task

TEST_INSTRUCTIONS = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def test_first_task() -> None:
    assert first_task(TEST_INSTRUCTIONS) == 40


def test_second_task() -> None:
    assert second_task(TEST_INSTRUCTIONS) == 315
