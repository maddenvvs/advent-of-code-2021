from aoc2021.day_05 import first_task, second_task, Line, Point

TEST_LINES = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_horizontal_line_points() -> None:
    line = Line(Point(0, 0), Point(5, 0))

    points = list(line)

    assert points == [Point(i, 0) for i in range(6)]


def test_vertical_line_points() -> None:
    line = Line(Point(7, 4), Point(7, 8))

    points = list(line)

    assert points == [Point(7, i) for i in range(4, 9)]


def test_diagonal_line_from_upper_left_to_lower_right_points() -> None:
    line = Line(Point(1, 1), Point(5, 5))

    points = list(line)

    assert points == [Point(i, i) for i in range(1, 6)]


def test_diagonal_line_from_lower_left_to_upper_right_points() -> None:
    line = Line(Point(1, 5), Point(5, 1))

    points = list(line)

    assert points == [Point(i, 6 - i) for i in range(1, 6)]


def test_first_task() -> None:
    assert first_task(TEST_LINES) == 5


def test_second_task() -> None:
    assert second_task(TEST_LINES) == 12
