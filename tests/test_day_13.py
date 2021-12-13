from aoc2021.day_13 import first_task, second_task

TEST_ORIGAMI = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_first_task() -> None:
    assert first_task(TEST_ORIGAMI) == 17


def test_second_task() -> None:
    assert (
        second_task(TEST_ORIGAMI)
        == """
#####
#...#
#...#
#...#
#####"""
    )
