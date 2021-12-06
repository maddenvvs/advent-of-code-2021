from importlib import import_module
from typing import Optional, Protocol, cast


def solution_module_name(day: int) -> str:
    return f"day_{day:02}"


class SupportsSolutions(Protocol):
    def first_task(self, text: str) -> str:
        ...

    def second_task(self, text: str) -> str:
        ...


def get_solution(day: int) -> Optional[SupportsSolutions]:
    module_name = solution_module_name(day)

    try:
        return cast(SupportsSolutions, import_module(f".{module_name}", "aoc2021"))
    except ModuleNotFoundError:
        return None
