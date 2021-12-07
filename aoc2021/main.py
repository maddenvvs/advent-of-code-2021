import click

from .loader import get_solution


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("day", type=click.IntRange(min=1, max=25))
@click.argument("file", type=click.Path(), required=False)
def cli(day: int, file: str) -> None:
    """AoC 2021 CLI application.

    Display solutions for DAY with problem input containing in FILE.
    """

    solution = get_solution(day)

    if solution is None:
        click.echo(f"There is no solution for day {day} yet. Stay tuned!")
        return

    if file is None:
        file = f"./input/day-{day:02}.input"

    with open(file, mode="r", encoding="utf-8") as file_stream:
        file_content = file_stream.read()

        click.echo(f"Day {day}-1: {solution.first_task(file_content)}")
        click.echo(f"Day {day}-2: {solution.second_task(file_content)}")
