from typing import Callable


def parse_crabs(crabs_text: str) -> list[int]:
    return [int(c) for c in crabs_text.split(",")]


def crab_simple_consumption(crab: int, position: int) -> int:
    return abs(crab - position)


def crab_advanced_consumption(crab: int, position: int) -> int:
    simple_consumption = crab_simple_consumption(crab, position)
    return simple_consumption * (simple_consumption + 1) // 2


def simple_fuel_consumption(crabs: list[int], position: int) -> int:
    return sum(crab_simple_consumption(crab, position) for crab in crabs)


def advanced_fuel_consumption(crabs: list[int], position: int) -> int:
    return sum(crab_advanced_consumption(crab, position) for crab in crabs)


def find_optimal_fuel_consumption(
    crabs: list[int], fuel_consumption: Callable[[list[int], int], int]
) -> int:
    left, right = min(crabs), max(crabs)
    consumption = fuel_consumption(crabs, right)

    while left + 1 < right:
        mid = left + (right - left) // 2
        mid_consumption = fuel_consumption(crabs, mid)
        mid_next_consumtion = fuel_consumption(crabs, mid + 1)

        if mid_consumption < mid_next_consumtion:
            consumption = mid_consumption
            right = mid
        else:
            left = mid

    return consumption


def first_task(crabs_text: str) -> int:
    return find_optimal_fuel_consumption(
        parse_crabs(crabs_text), simple_fuel_consumption
    )


def second_task(crabs_text: str) -> int:
    return find_optimal_fuel_consumption(
        parse_crabs(crabs_text), advanced_fuel_consumption
    )
