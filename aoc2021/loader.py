from importlib import import_module
from typing import Optional, Protocol, cast


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
