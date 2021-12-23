import pytest
from aoc2021.day_23 import Burrow, first_task, second_task


def test_burrow_example_last_step() -> None:
    test_burrow = """#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########"""
    burrow = Burrow.parse(test_burrow)

    assert burrow.find_min_energy() == 8


def test_burrow_example_two_last_steps() -> None:
    test_burrow = """#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########"""
    burrow = Burrow.parse(test_burrow)

    assert burrow.find_min_energy() == 7008


def test_burrow_example_three_last_steps() -> None:
    test_burrow = """#############
#.....D.D...#
###.#B#C#.###
  #A#B#C#A#
  #########"""
    burrow = Burrow.parse(test_burrow)

    assert burrow.find_min_energy() == 7011


def test_burrow_example_four_last_steps() -> None:
    test_burrow = """#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########"""
    burrow = Burrow.parse(test_burrow)

    assert burrow.find_min_energy() == 9011


def test_burrow_example_some_steps() -> None:
    test_burrow = """#############
#.....D...A.#
###.#B#C#.###
  #A#B#C#D#
  #########"""
    burrow = Burrow.parse(test_burrow)

    assert burrow.find_possible_moves_for("A1") == []


def test_burrow_2_last_step() -> None:
    test_burrow = """#############
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########"""
    burrow = Burrow.parse(test_burrow)

    assert burrow.find_min_energy() == 3000


def test_burrow_2_last_two_steps() -> None:
    test_burrow = """#############
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########"""
    burrow = Burrow.parse(test_burrow)

    assert burrow.find_min_energy() == 3008


@pytest.mark.skip(reason="Test is too slow")
def test_first_task() -> None:
    test_burrow = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

    assert first_task(test_burrow) == 12521


@pytest.mark.skip(reason="Test is too slow")
def test_second_task() -> None:
    test_burrow = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

    assert second_task(test_burrow) == 44169
