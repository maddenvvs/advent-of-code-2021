from functools import cache


@cache
def count_fishes_2d(fish, days):
    if fish >= days:
        return 1

    remaining_days = days - fish - 1
    return count_fishes_2d(6, remaining_days) + count_fishes_2d(8, remaining_days)


@cache
def count_fishes_1d(days):
    if days < 1:
        return 1

    return count_fishes_1d(days - 7) + count_fishes_1d(days - 9)


def count_fishes_iterative(days):
    order = 9
    fishes = [1] * order

    for day in range(1, days + 1):
        fishes[day % order] = fishes[(day - 7) % order] + fishes[(day - 9) % order]

    return fishes[days % order]


def number_of_fishes(fishes: list[int], days: int) -> int:
    return sum(count_fishes_iterative(days - fish) for fish in fishes)


def parse_fishes(fishes_text: str) -> list[int]:
    return [int(i) for i in fishes_text.split(",")]


def first_task(fishes_text: str) -> int:
    return number_of_fishes(parse_fishes(fishes_text), 80)


def second_task(fishes_text: str) -> int:
    return number_of_fishes(parse_fishes(fishes_text), 256)
