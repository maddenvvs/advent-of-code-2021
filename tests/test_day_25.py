from aoc2021.day_25 import Region, first_task

TEST_CUCUMBERS = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""


def test_region_one_step_only_east() -> None:
    region = Region.parse("""...>>>>>...""")

    region.simulate_step()

    assert str(region) == "...>>>>.>.."


def test_region_second_step_only_east() -> None:
    region = Region.parse("""...>>>>>...""")
    region.simulate_step()

    region.simulate_step()

    assert str(region) == "...>>>.>.>."


def test_region_four_cucumbers() -> None:
    region = Region.parse(
        """..........
.>v....v..
.......>..
.........."""
    )

    region.simulate_step()

    assert (
        str(region)
        == """..........
.>........
..v....v>.
.........."""
    )


def test_region_strong_water_currents() -> None:
    region = Region.parse(
        """...>...
.......
......>
v.....>
......>
.......
..vvv.."""
    )

    region.simulate_step()

    assert (
        str(region)
        == """..vv>..
.......
>......
v.....>
>......
.......
....v.."""
    )


def test_first_task() -> None:
    assert first_task(TEST_CUCUMBERS) == 58
