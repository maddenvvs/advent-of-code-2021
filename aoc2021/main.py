from importlib import import_module
from typing import TextIO, Optional, Protocol, cast

import click


class SupportsSolutions(Protocol):
    def first_task(self, text: str) -> str:
        ...

    def second_task(self, text: str) -> str:
        ...


def get_solution(day: int) -> Optional[SupportsSolutions]:
    try:
        return cast(SupportsSolutions, import_module(f".day_{day:02}", "aoc2021"))
    except ModuleNotFoundError:
        return None


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("day", type=click.IntRange(min=1, max=25))
@click.argument("file", type=click.File("r"))
def cli(day: int, file: TextIO) -> None:
    """AoC 2021 CLI application.

    Display solutions for DAY with problem input containing in FILE.
    """

    solution = get_solution(day)

    if solution is None:
        click.echo(f"There is no solution for day {day} yet. Stay tuned!")
        return

    file_content = file.read()

    click.echo(f"Day {day}-1: {solution.first_task(file_content)}")
    click.echo(f"Day {day}-2: {solution.second_task(file_content)}")
