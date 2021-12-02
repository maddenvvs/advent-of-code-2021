from dataclasses import dataclass
from functools import reduce
from typing import Iterable, NamedTuple


class Command(NamedTuple):
    operation: str
    value: int


@dataclass(slots=True)
class SubmarineState:
    position: int = 0
    depth: int = 0
    aim: int = 0


def first_reducer(state: SubmarineState, action: Command) -> SubmarineState:
    match action:
        case Command("forward", value):
            state.position += value
        case Command("up", value):
            state.depth -= value
        case Command("down", value):
            state.depth += value
        case _:
            raise Exception("Unknown command: ", action)
    return state


def second_reducer(state: SubmarineState, action: Command) -> SubmarineState:
    match action:
        case Command("forward", value):
            state.position += value
            state.depth += value * state.aim
        case Command("up", value):
            state.aim -= value
        case Command("down", value):
            state.aim += value
        case _:
            raise Exception("Unknown command: ", action)
    return state


def parse_program(text: str) -> Iterable[Command]:
    for command in text.split("\n"):
        operation, value_str = command.split()
        value = int(value_str, base=10)
        yield Command(operation, value)


def first_task(program_text: str) -> int:
    state = reduce(first_reducer, parse_program(program_text), SubmarineState())
    return state.position * state.depth


def second_task(program_text: str) -> int:
    state = reduce(second_reducer, parse_program(program_text), SubmarineState())
    return state.position * state.depth
