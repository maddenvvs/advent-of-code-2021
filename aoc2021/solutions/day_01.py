from .solution import Solution


def parse_entries(text: str) -> list[int]:
    return [int(i) for i in text.split()]


def first_task(depths: list[int]) -> int:
    if len(depths) < 2:
        return 0

    return sum(depths[i] > depths[i - 1] for i in range(1, len(depths)))


def second_task(depths: list[int], window_size: int = 3) -> int:
    if len(depths) <= window_size:
        return 0

    curr_window = sum(depths[i] for i in range(window_size))
    next_window, increases = curr_window, 0

    for i in range(window_size, len(depths)):
        next_window += depths[i] - depths[i - window_size]
        increases += next_window > curr_window
        curr_window = next_window

    return increases


class Day01(Solution):
    def first_task(self, entries_text: str) -> str:
        entries = parse_entries(entries_text)

        return str(first_task(entries))

    def second_task(self, entries_text: str) -> str:
        entries = parse_entries(entries_text)

        return str(second_task(entries))
