import pytest
from aoc2021.day_11 import first_task, second_task, Grid

TEST_GRID = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


@pytest.mark.parametrize(
    "curr_grid,next_grid",
    [
        (
            """11111
19991
19191
19991
11111""",
            """34543
40004
50005
40004
34543""",
        ),
        (
            """34543
40004
50005
40004
34543""",
            """45654
51115
61116
51115
45654""",
        ),
        (
            """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637""",
            """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848""",
        ),
    ],
)
def test_one_step_simulation(curr_grid: str, next_grid: str) -> None:
    grid = Grid.parse(curr_grid)

    grid.simulate_one_step()

    assert str(grid) == next_grid


@pytest.mark.parametrize("steps,expected_flashes", [(10, 204), (100, 1656)])
def test_flashes_after(steps: int, expected_flashes: int) -> None:
    grid = Grid.parse(TEST_GRID)

    flashes = grid.simulate_multiple_steps(steps)

    assert flashes == expected_flashes


def test_first_task() -> None:
    assert first_task(TEST_GRID) == 1656


def test_second_task() -> None:
    assert second_task(TEST_GRID) == 195
